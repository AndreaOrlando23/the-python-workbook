# EXERCISE 40 : Sound Levels

JACKHAMMER = 130
GAS_LAWNMOWER = 106
ALARM_CLOCK = 70
QUIET_ROOM = 40

sound_level = float(input('Enter the sound level in decibel: '))

# First control - guardian
if sound_level < QUIET_ROOM:
    print('The sound level is less than a Quiet room')
elif sound_level > JACKHAMMER:
    print('The sound level is greater than a Jackhammer')

# sound level equal to indexes
elif sound_level == QUIET_ROOM:
    print('Sound level: Quiet room')
elif sound_level == ALARM_CLOCK:
    print('Sound level: Alarm clock')
elif sound_level == GAS_LAWNMOWER:
    print('Sound level: Gas lawnmower')
elif sound_level == JACKHAMMER:
    print('Sound level: Jackhammer')

# sound level between indexes
elif QUIET_ROOM < sound_level < ALARM_CLOCK:
    print('The sound level is between of Quiet room and Alarm clock')
elif ALARM_CLOCK < sound_level < GAS_LAWNMOWER:
    print('The sound level is between of Alarm clock and Gas lawnmower')
elif GAS_LAWNMOWER < sound_level < JACKHAMMER:
    print('The sound level is between of Gas lawnmower and Jackhammer')
