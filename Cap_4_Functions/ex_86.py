# EXERCISE 86 : Taxi Fare

BASE_FARE = 4
PLUS = 0.25


def bill(km):
    km_to_meter = km * 1000
    plus_fare = km_to_meter // 140 * PLUS

    if km_to_meter // 140 < 1:
        return BASE_FARE

    return plus_fare + BASE_FARE


def main():
    distance = int(input("Enter the distance travelled: "))
    total = bill(distance)
    print(f"The total fare is: {total}")


main()
