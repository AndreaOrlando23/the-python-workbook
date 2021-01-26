# EXERCISE 181 : Possible Change
# TODO


# Function to find the total number of distinct ways to get change of N
# from unlimited supply of coins in set S
def count(coins, n, dollars):
    # if total is 0, return 1 (solution found)
    if dollars == 0:
        return 1

    # return 0 (solution do not exist) if total become negative or
    # no elements are left
    if dollars < 0 or n < 0:
        return 0

    # Case 1. include current coin coins[n] in solution and recur
    # with remaining change (dollars - coins[n]) with same number of coins
    incl = count(coins, n, dollars - coins[n])

    # Case 2. exclude current coin coins[n] from solution and recur
    # for remaining coins (n - 1)
    excl = count(coins, n - 1, dollars)

    # return total ways by including or excluding current coin
    return incl + excl


def main():
    # n coins of given denominations
    coins = [0.01, 0.05, 0.10, 0.25]

    # Total Change required
    dollar = float(input("Enter the amount of dollars: "))
    coin = int(input("Enter the number of coin: "))

    result = count(coins, len(coins) - 1, dollar)

    if result <= coin:
        print(f"I can change your amount of dollars with {coin} coins")
    else:
        print(f"ERROR: I can't change your amount of dollars with {coin} coins")



main()
