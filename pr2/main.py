import math


def func(x):
    if x < 86:
        return (math.e ** (x ** 3)) + (x ** 7)
    elif 86 <= x & x < 160:
        return ((x ** 4) / 78) - ((x ** 2) / 8)
    elif 160 <= x & x < 188:
        return 45 * x - x ** 8
    elif x >= 188:
        return math.tan(x - 68 * (x ** 7)) + 30 * (x ** 8)


if __name__ == '__main__':
    print ("%.2e" %  (math.e ** (85 ** 3)) + (85 ** 7))
