# EXERCISE 36 : Dog years

human_age = int(input('Enter your age: '))

# conversion of the first two humans age to dogs age is 21. After that, 4 years dogs age == 1 year human age
first_two_years = 10.5
dogs_age = (human_age - 2) * 4 + first_two_years * 2

if human_age <= 0:
    print('ERROR: The human age must be positive and greater then 0')
elif human_age == 1 or human_age == 2:
    print('The conversion from human age to dog age is:', human_age * first_two_years)
else:
    print('The conversion from human age to dog age is: %i' % dogs_age)
