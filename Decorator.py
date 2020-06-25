"""
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""


def dec(sum):
    lst = []

    def wrapper(*args, **kwargs):
        nonlocal lst
        res = sum(*args, **kwargs)
        lst.append(res)
        f = open('log.txt', 'a')
        f.write(str(lst))
        f.close()
        # print(lst)
        return lst
    return wrapper


@dec
def sum(*b):
    sum = 0
    for i in b:
        sum += i
    return sum


print(sum(1, 5))
print(sum(2, 5, 6))
print(sum(11, 5))
