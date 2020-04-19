import math


def root_function(a, b, c):
    if b ** 2 - 4 * a * c > 0:
        print((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2*a, (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2*a)
    elif b ** 2 - 4 * a * c == 0:
        print((-b + math.sqrt(b ** 2 - 4 * a * c) / 2*a))
    else:
        print("there is no root in the function")


a = int(input())
b = int(input())
c = int(input())
root_function(a, b, c)
