import math


def f11(x, y):
    res = (97 * (y ** 6) - (math.e ** x) + 72) / (y + ((y ** 2) / 53) + 35) - math.sqrt(
        (86 * (y ** 8) + ((x ** 3) / 51)) / ((69 * (x ** 6)) + math.sin(y))) + 47 * (x ** 8) - (y ** 4) - 25
    return "%.2e" % res


def f12(x):
    if x < 86:
        return (math.e ** (x ** 3)) + (x ** 7)
    elif 86 <= x & x < 160:
        return ((x ** 4) / 78) - ((x ** 2) / 8)
    elif 160 <= x & x < 188:
        return 45 * x - x ** 8
    elif x >= 188:
        return "%.2e" % (math.tan(x - 68 * (x ** 7)) + 30 * (x ** 8))


def f13(n, m):
    return "%.2e" % (92 * sum(n, m) - sum2(n))


def sum(n, m, k=0):
    for i in range(1, n+1, 1):
        for j in range(1, m+1, 1):
            k += (math.e ** j + i ** 3)
    return k


def sum2(n, k=0):
    for i in range(1, n+1, 1):
        k += ((math.log(i, math.e) - ((i ** 7) / 3)) + 5)
    return k


def f14(n):
    if n == 0:
        return 7
    else:
        return "%.2e" % ((1 / 95) * func(n - 1) + (1 / 85) * ((func(n - 1)) ** 2))

