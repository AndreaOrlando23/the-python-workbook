# EXERCISE 108 : Reduce measures
# TODO

TSP = 1
TSP_PER_TBSP = TSP * 3
TSP_PER_CUP = TSP_PER_TBSP * 16


def reduce_measure(num, unit):
    # Convert the unit to lowercase
    unit = unit.lower()

    # Compute the number of teaspoons that the parameters represent
    if unit == "teaspoon" or unit == "teaspoons":
        teaspoons = num
    elif unit == "tablespoon" or unit == "tablespoons":
        teaspoons = num * TSP_PER_TBSP
    elif unit == "cup" or unit == "cups":
        teaspoons = num * TSP_PER_CUP

    # Convert the number of teaspoons to the largest possible units measure
    cups = teaspoons // TSP_PER_CUP
    teaspoons = teaspoons - cups * TSP_PER_CUP
    tablespoons = teaspoons // TSP_PER_TBSP
    teaspoons = teaspoons - tablespoons * TSP_PER_TBSP

    # Create a string to hold the result
    result = ""

