import math


def func(n, m):
    #print (sum2(n))
    return 92 * sum(n, m) - sum2(n)


def sum(n, m, k=0):
    for i in range(1, n+1, 1):
        for j in range(1, m+1, 1):
            k += (math.e ** j + i ** 3)
    return k


def sum2(n, k=0):
    for i in range(1, n+1, 1):
        k += ((math.log(i, math.e) - ((i ** 7) / 3)) + 5)
    return k


if __name__ == '__main__':
    print("%.2e" % func(68, 16))
    print("%.2e" % func(97, 80))
