"""
Напишите программу, которая печатает цифры от 1 до 100,
но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратныХ 5 пишет Buzz,
а вместо чисел одновременно кратных и 3, и 5 - FizzBuzz
"""

for i in range(1, 101):
    if not i % 15:
        print("FizzBuzz", end=" ")
    elif not i % 3:
        print("Fizz", end=" ")
    elif not i % 5:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
