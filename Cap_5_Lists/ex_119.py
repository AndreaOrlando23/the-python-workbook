# Below and Above Average
from statistics import mean


def average(data):
    avg = mean(data)
    below_avg = []
    above_avg = []

    for num in data:
        if num < avg:
            below_avg.append(num)
        elif num > avg:
            above_avg.append(num)

    print(f"Values below the average: {below_avg}")
    print(f"Average: {avg}")
    print(f"Values above the average: {above_avg}")


def main():
    numbers = []
    line = input("Enter an integer number (blank to quit): ")

    while line != "":
        n = int(line)
        numbers.append(n)
        line = input("Enter an integer number (blank to quit): ")

    average(numbers)


main()