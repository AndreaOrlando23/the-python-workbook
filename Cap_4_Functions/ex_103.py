# EXERCISE 103 : Random good password
from ex_100 import random_password
from ex_102 import check_password


def random_good_pw():
    rand_pw = random_password()
    attempts = 1

    while check_password(rand_pw):
        rand_pw = random_password()
        attempts += 1
    
    print(f"attempts: {attempts}\nPassword: {rand_pw}")


random_good_pw()
