"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
a.	runner() – все фукнции вызываются по очереди
b.	runner(‘func_name’) – вызывается только функцию func_name.
c.	runner(‘func’, ‘func1’...) - вызывает все переданные функции

"""
import funcs


def runner(*args):
    # print(*args)
    if len(args) == 0:
        for name in dir(funcs):
            if '__' not in name:
                f = getattr(funcs, name)
                f()
    else:
        # print(args)
        for arg in args:
            if arg in dir(funcs):
                a = getattr(funcs, arg)
                a()


runner()
# print(dir(funcs))
runner('gcf')
runner('sum', 'gcf')
