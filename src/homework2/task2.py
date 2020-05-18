"""Найти самое длинное слово в введенном предложении. В случае если их
    несколько, самое левое в строке Учтите что в предложении есть знаки
    препинания.
"""


def longest_word(str_):
    """Поиск самого длинного слова в предложении.

    :param str_: входная строка
    :return: строка. Самое длинное слово в предложении (в случае если их
        несколько, самое левое в строке).
        в случае если
    """
    # write your code here
    list = str_.split()
    new_list = []
    for i in list:
        new_list.append(i.strip(',.:!@?'))
    longest_word = new_list[0]
    for i in new_list:
        if len(i) > len(longest_word):
            longest_word = i
    return longest_word  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = input("Input your string: ")
    print(longest_word(str_))
