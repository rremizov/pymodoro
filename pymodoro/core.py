import urwid

import pymodoro.views


class Application:
    def __init__(self):
        self.mainloop = None
        self.root = None

    def reset_root_widget(self, top_w):
        self.root = urwid.Overlay(
            top_w,
            urwid.SolidFill(' '),
            align='center',
            width=('relative', 80),
            valign='middle',
            height=('relative', 90),
            min_width=20,
            min_height=9)

        if self.mainloop is not None:
            self.mainloop.widget = self.root

    def exit(self, delay=None):
        if delay is None:
            raise urwid.ExitMainLoop()

        self.mainloop.set_alarm_in(int(delay), lambda *_: self.exit())

    def exit_on_q(self, key):
        if key not in ('q', 'Q'):
            return

        self.exit()


def entry_point():
    app = Application()

    root_widget = pymodoro.views.MainMenu(app)
    app.reset_root_widget(root_widget)

    app.mainloop = urwid.MainLoop(
        app.root,
        palette=[('reversed', 'standout', ''),
                 ('underline', 'underline', '')],
        unhandled_input=app.exit_on_q)
    app.mainloop.run()
