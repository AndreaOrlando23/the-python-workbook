from time import Time


start = Time()
start.hour = 9
start.minute = 45
start.second = 0


def main():
    Time.print_time(start)
    # method syntax - call print_time in a more concisely version
    start.print_time()

    end = start.increment(1337)
    Time.print_time(end)
    end.print_time()
    print(end.is_after(start))

    time = Time(9, 45, 12)
    time.print_time()


if __name__ == '__main__':
    main()
