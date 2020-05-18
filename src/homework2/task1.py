"""Напишите программу, которая считает общую цену. Вводится M рублей и N копеек,
 а также количество S товара Посчитайте общую цену в рублях и копейках
   за L товаров.
"""


def total_sum(m, n, s):
    """Подсчет общей суммы покупок.
    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    # write your code here
    m, n, s = int(m), int(n), int(s)
    price = (m * 100 + n) * s  # in kopecks
    rubles = price // 100
    kopecks = price % 100
    return print("Total price:", rubles, "rubles", kopecks, "kopecks")   # write return value here
    #return rubles,kopecks


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = input("Enter roubles, kopecks, quantity of goods separated by space: ").split()
    print(total_sum(m, n, s))
