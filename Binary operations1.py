"""
Написать программу которая находит ближайшую степень двойки
к введенному числу. 10(8), 20(16), 1(1), 13(16)
"""


def near_pow2(n):
    num = n
    pow = 0
    while n > 1:
        n = n >> 1
        pow += 1

    if abs(num - 2 ** pow) < abs(num - 2 ** (pow + 1)):
        return 2 ** pow
    else:
        return 2 ** (pow + 1)


# for test
# def is_pow2(word):
#   return word & (word - 1) == 0


n = int(input("Enter number: "))
x = near_pow2(n)
print(x)
