"""
Дан список стран и городов каждой страны. Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк,
каждая строка начинается с названия страны, затем идут названия
городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов,
перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны,
в котором находится данный город.
Примеры
Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod

Выходные данные
Ukraine
Russia
Russia
"""


def input_data():
    # dictionary for data storage
    dct = {}

    N = int(input("Input number of countries: "))

    while N > 0:
        # entering data
        country, *cities = input("Enter country and cities names: ").split()
        # entering data into a dictionary
        dct[country] = tuple(cities)
        # to prevent endless loop
        N -= 1
    return dct


def output_data(dct):
    # list for storing found countries
    country = []
    # list for dictionary mirroring
    s = []
    # the second mirror dict
    for i in dct.keys():
        s.append((dct[i], i))
    tcd = dict(s)

    M = int(input("Input number of cities: "))

    while M > 0:
        cities = input("Enter cities names: ")
        # search for the input city in a nested loop
        # and add it to the list
        for i in tcd:
            for j in i:
                if cities == j:
                    country.append(tcd[i])
        # to prevent endless loop
        M -= 1
    # print(country) # for test
    # The final output of the cities
    for i in country:
        print(i)


x = input_data()
# for test
# print(x)
output_data(x)
