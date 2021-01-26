# EXERCISE 135 : The Sieve of Eratosthenes

limit = int(input("Identify all primes up to what limit? "))

nums = []
for i in range(0, limit + 1):
    nums.append(i)

nums[1] = 0

p = 2

while p < limit:
    for i in range(p*2, limit + 1, p):
        nums[i] = 0

    p += 1
    while p < limit and nums[p] == 0:
        p += 1

print(f"The prime up to {limit} are:")
for i in nums:
    if nums[i] != 0:
        print(i)

