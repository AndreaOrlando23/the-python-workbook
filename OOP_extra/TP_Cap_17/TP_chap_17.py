# from TP_chap_16 import int_to_time
from time import Time

class Time:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


start = Time()
start.hour = 9
start.minute = 45
start.second = 0


def main():
    Time.print_time(start)
    # method syntax - call print_time in a more concise version
    start.print_time()

    end = start.increment(1337)
    Time.print_time(end)
    end.print_time()
    print(end.is_after(start))

    time = Time(9, 45, 12)
    time.print_time()


if __name__ == '__main__':
    main()
