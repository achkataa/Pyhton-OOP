import datetime

# #
# x = datetime.datetime.
#
# print(x.strftime("%X"))

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        time = f"{self.hours}:{self.minutes}:{self.seconds}"


