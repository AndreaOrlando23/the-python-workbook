# EXERCISE 128 : Count the Element

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_val = 2
max_val = 8


def count_range(list_values, minimum, maximum):
    cluster_list = []
    for n in list_values:
        if minimum <= n < maximum:
            cluster_list.append(n)

    cluster = len(cluster_list)
    return cluster


def main():
    cluster = count_range(numbers, min_val, max_val)
    if cluster > 0:
        print(f"The cluster is: {cluster}")


main()
