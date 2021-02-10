import math


def func(x, y):
    res = (97 * (y ** 6) - (math.e ** x) + 72) / (y + ((y ** 2) / 53) + 35) - math.sqrt(
        (86 * (y ** 8) + ((x ** 3) / 51)) / ((69 * (x ** 6)) + math.sin(y))) + 47 * (x ** 8) - (y ** 4) - 25
    return res


if __name__ == '__main__':
    print("%.2e" % func(87, 54))
    print("%.2e" % func(-74, -98))
