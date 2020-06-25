def gcf(a = 33, b = 11):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)


def sum(*b):
    sum = 0
    for i in b:
        sum += i
    print(sum)


if __name__ == '__main__':
    gcf(99, 66)


