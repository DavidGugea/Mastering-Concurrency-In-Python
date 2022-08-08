from math import sqrt


def is_prime(x):
    print("Processing {0}".format(x))

    if x < 2:
        print("{0} is not a prime number".format(x))
    elif x == 2:
        print("{0} is a prime number".format(x))
    elif x % 2 == 0:
        print("{0} is not a prime number".format(x))
    else:
        limit = int(sqrt(x)) + 1

        for i in range(3, limit, 2):
            if x % i == 0:
                print("{0} is not a prime number.".format(x))
                return

        print("{0} is a prime number".format(x))
