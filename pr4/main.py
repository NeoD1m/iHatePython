def func(n):
    if n == 0:
        return 7
    else:
        return (1 / 95) * func(n - 1) + (1 / 85) * ((func(n - 1)) ** 2)


if __name__ == '__main__':
    print("%.2e" % func(16))
    print("%.2e" % func(10))
