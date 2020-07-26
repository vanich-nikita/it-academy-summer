"""
Создайте декоратор, который вызывает задекорированную функцию пока она
не выполнится без исключений (но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение
типа TooManyErrors.
"""


class TooManyErrors(Exception):
    pass


def my_dec(times):

    def dec(func):
        nonlocal times

        def wrapper(*args, **kwargs):
            nonlocal times
            res = 0
            try:
                if not times:
                    raise TooManyErrors()
                res = func(*args, **kwargs)
                print(res)
                times -= 1
            except TooManyErrors:
                print("TooManyErrors - Calls ended")
            return res
        return wrapper
    return dec


if __name__ == '__main__':
    @my_dec(3)
    def fun(a=0, b=0):
        return a + b
    fun(22, 4)
    fun(1, 4)
    fun(5, 6)
    fun()
    fun()
