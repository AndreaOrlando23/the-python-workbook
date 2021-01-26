# EXERCISE 103 : Random good password
# TODO

from ex_102 import check_password


def random_good_pw():
    rand_pw = random_password()

    for pw in range(50):
        if check_password(rand_pw):
            print(pw, end=" --> ")
            print(rand_pw)


random_good_pw()
