import copy
from time import Time


def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def increment(time, seconds):
    my_time = copy.deepcopy(time)  # create a copy of time object passed
    tot_seconds = time_to_int(my_time) + seconds

    return int_to_time(tot_seconds)


# start time of a movie
start = Time()
start.hour = 9
start.minute = 45
start.second = 0

# run time of a movie
duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0


done = add_time(start, duration)
# print_time(done)


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 12
time2.minute = 59
time2.second = 30