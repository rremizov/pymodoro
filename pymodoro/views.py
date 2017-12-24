import subprocess

import urwid

import pymodoro.cli
import pymodoro.configuration
import pymodoro.logger
import pymodoro.pomodoro
import pymodoro.utils


class MainMenu(urwid.ListBox):

    def keypress(self, size, key):
        if key == 'j':
            key = 'down'
        elif key == 'k':
            key = 'up'

        return super(MainMenu, self).keypress(size, key)

    def __init__(self, app):
        self.app = app

        body = [
            StartPomodoroButton(app),
            StartShortBreakButton(app),
            StartLongBreakButton(app),
        ]

        super(MainMenu, self).__init__(urwid.SimpleListWalker(body))


class StartTimerButton(urwid.Button):
    LABEL = None

    def __init__(self, app):
        self.app = app
        super(StartTimerButton, self).__init__(self.LABEL, self.on_press)

    def on_press(self, button):
        raise NotImplementedError()


class StartPomodoroButton(StartTimerButton):
    LABEL = 'Pomodoro'

    def on_press(self, button):
        self.app.reset_root_widget(
            PomodoroTimer(
                self.app,
                pymodoro.pomodoro.Pomodoro(),
                'Focus, pomodoro is running!',
                'Take a break!',
            ))


class StartShortBreakButton(StartTimerButton):
    LABEL = 'Short break'

    def on_press(self, button):
        self.app.reset_root_widget(
            PomodoroTimer(
                self.app,
                pymodoro.pomodoro.ShortBreak(),
                'Take a short break!',
                'Short break has ended!',
            ))


class StartLongBreakButton(StartTimerButton):
    LABEL = 'Long break'

    def on_press(self, button):
        self.app.reset_root_widget(
            PomodoroTimer(
                self.app,
                pymodoro.pomodoro.LongBreak(),
                'Take a long break, you deserve it!',
                'Long break has ended!',
            ))


class PomodoroTimer(urwid.ListBox):

    def __init__(self, app, pomodoro_timer, body_text, notification_text):
        self.app = app
        self.pomodoro_timer = pomodoro_timer
        self.body_text = body_text
        self.notification_text = notification_text
        self.list_walker = urwid.SimpleListWalker([])

        super(PomodoroTimer, self).__init__((self.list_walker))

        self.__update()

    def __schedule_update(self):
        self.app.mainloop.set_alarm_in(1, self.__update)

    def __update(self, *args, **kwargs):
        if self.pomodoro_timer.has_ended:
            subprocess.call([
                'notify-send', '--urgency', 'critical', 'Pymodoro', self.notification_text
            ])
            self.app.reset_root_widget(pymodoro.views.MainMenu(self.app))
            return

        self.__render()
        self.__schedule_update()

    def __render(self):
        minutes_left = self.pomodoro_timer.minutes_left
        seconds_left = self.pomodoro_timer.seconds_left
        time_left = '{}m. {}s.'.format(minutes_left, seconds_left)

        self.list_walker[:] = [
            urwid.Button('Back', self.__on_press_back),
            urwid.Text(('underline', self.body_text)),
            urwid.Text('Time left: {}'.format(time_left)),
        ]

    def __on_press_back(self, button):
        self.app.reset_root_widget(pymodoro.views.MainMenu(self.app))
