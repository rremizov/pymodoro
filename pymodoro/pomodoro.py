from datetime import datetime, timedelta


class Timer:
    DURATION = None

    def __init__(self):
        self.start_at = datetime.now()

    @property
    def has_ended(self):
        return self.time_passed > self.DURATION

    @property
    def time_passed(self):
        return datetime.now() - self.start_at

    @property
    def time_left(self):
        return self.DURATION - self.time_passed

    @property
    def minutes_left(self):
        return int(self.time_left.total_seconds() / 60)

    @property
    def seconds_left(self):
        return int(self.time_left.total_seconds() % 60)


class Pomodoro(Timer):
    DURATION = timedelta(minutes=25)


class ShortBreak(Timer):
    DURATION = timedelta(minutes=5)


class LongBreak(Timer):
    DURATION = timedelta(minutes=15)
