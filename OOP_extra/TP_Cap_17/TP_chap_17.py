from class_time import Time


def main():
    # Time.print_time(start)
    # method syntax - call print_time in a more concisely version
    # start.print_time()

    start = Time(9, 45, 0)
    end = start.increment(1337)

    # Time.print_time(end)
    # end.print_time()
    result = start.is_after(end)
    print(result)

    # time = Time(9, 45, 12)
    # time.print_time()


if __name__ == '__main__':
    main()
