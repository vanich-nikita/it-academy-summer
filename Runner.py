"""
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
a.	runner() – все фукнции вызываются по очереди
b.	runner(‘func_name’) – вызывается только функцию func_name.
c.	runner(‘func’, ‘func1’...) - вызывает все переданные функции

"""
import funcs


def check_name(func_name):
    if not func_name.startswith('__') and not func_name.endswith('__'):
        f = getattr(funcs, func_name)
        return f()


def runner(*args):
    if len(args) == 0:
        for name in dir(funcs):
            check_name(name)
    else:
        for arg in args:
            if arg in dir(funcs):
                check_name(arg)
            else:
                print("Unknown function")


runner()
runner('gcf')
runner('sum', 'gcf')
runner(__name__)
runner(11)
