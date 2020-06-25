"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""


def maximum_divisor(n):
    pow = 1
    max_divisor = 1
    while n >= pow:
        pow = pow << 1
        if n % pow == 0:
            max_divisor = pow
    return max_divisor


n = int(input("Enter number: "))
x = maximum_divisor(n)
print(x)
