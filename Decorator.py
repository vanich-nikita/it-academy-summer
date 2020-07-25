"""
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""
from datetime import datetime


def dec(func):

    def wrapper(*args, **kwargs):
        now = datetime.now()
        current_time = now.strftime("%D %H:%M:%S ")
        res = func(*args, **kwargs)
        f = open("log.txt", "a")
        f.write(current_time + func.__name__ + " from arguments: positional"
                " {} keyword {} is ".format(args, kwargs) + str(res) + '\n')
        f.close()
        return res
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
