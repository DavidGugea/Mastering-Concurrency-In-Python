from operator import mul
from functools import reduce

try:
    while True:
        line = input("Please enter a list of integer, separated by commas:")

        try:
            nums = list(map(int, line.split(', ')))
        except ValueError:
            print("ERROR. Enter only integers separated by commas")
            continue

        print("Sum of input integers {0}".format(sum(nums)))
        print("Product of input integers {0}".format(reduce(mul, nums, 1)))
except KeyboardInterrupt:
    print("\nFinished")
