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
        country, *cities = input("Enter country and cities names: ").split()
        dct[country] = tuple(cities)
        N -= 1
    return dct


def output_data(dct):
    # list for storing found countries
    country = []
    # list for dictionary mirroring
    mirror_list = []
    # the second mirror dict
    for state in dct.keys():
        mirror_list.append((dct[state], state))
    tcd = dict(mirror_list)

    M = int(input("Input number of cities: "))

    while M > 0:
        cities = input("Enter cities names: ")
        # search for the input city in a nested loop
        # and add it to the list
        for towns in tcd:
            for town in towns:
                if cities == town:
                    country.append(tcd[towns])
        M -= 1
    # The final output of the cities
    for state in country:
        print(state)


input_data = input_data()
output_data(input_data)
