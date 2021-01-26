# EXERCISE 25 : Units of time (again)

SECONDS_PER_DAY = 86400
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTES = 60

seconds = int(input('Enter a number of seconds: '))

days = seconds / SECONDS_PER_DAY
seconds = seconds % SECONDS_PER_DAY

hours = seconds / SECONDS_PER_HOUR
seconds = seconds % SECONDS_PER_HOUR

minutes = seconds / SECONDS_PER_MINUTES
seconds = seconds % SECONDS_PER_MINUTES


print('The equivalent duration is %02d:%02d:%02d:%02d' % (days, hours, minutes, seconds))
