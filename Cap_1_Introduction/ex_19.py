# EXERCISE 19 : Free Fall
import math

GRAVITY = 9.8

distance = float(input('Height (in meters): '))
final_speed = math.sqrt(2 * GRAVITY * distance)

print('The final speed is %.2f' % final_speed)
