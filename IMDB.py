"""
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле
./data5/ ratings.list.
a.	Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
b.	Найдите ТОП250 фильмов и извлеките заголовки.
c.	Программа создает 3 файла  top250_movies.txt
– названия файлов, ratings.txt – гистограмма рейтингов,
years.txt – гистограмма годов.
"""

import os

END_OF_OUR_ZONE_OF_INTEREST = 278
TRASH_IN_THE_BEGINNING = 26

try:
    # open the original file
    f = open('ratings.list', 'r')
    # variable for working with text
    a = ''
    # counter to perform the desired number of repetitions
    counter1 = 1
    for i in f:
        while counter1 < END_OF_OUR_ZONE_OF_INTEREST:
            a = str(f.readline())
            top250 = open('top250.txt', 'a')
            top250.write(a)
            top250.close()
            counter1 += 1
    f.close()

    top250 = open('top250.txt', 'r')
    counter2 = 1
    # skip the lines at the beginning of the file
    for i in top250:
        while counter2 < TRASH_IN_THE_BEGINNING:
            a = str(top250.readline())
            counter2 += 1
        a = str(top250.readline())
        while a != '':
            top250_temp = open('top250_movies_temp.txt', 'a')
            a = str(top250.readline())
            top250_temp.write(a)
    top250_temp.close()
    top250.close()

    os.remove('top250.txt')
    os.rename('top250_movies_temp.txt', 'top250_1.txt')

    # further we form the dictionaries
    # initial dict
    counter3 = 1
    dct = {}
    f = open('top250_1.txt', 'r')
    # list to store strings
    lst = []
    a = str(f.readline())
    # we read the file to the end and break the values according to the words
    while a != '':
        for i in a.split():
            lst.append(i)
            dct[counter3] = lst
        counter3 += 1
        lst = []
        a = str(f.readline())
    f.close()

    os.remove('top250_1.txt')

    # print(dct)
    # movie title dictionary
    dct_names = {}
    for number, initial_list in dct.items():
        for element in initial_list:
            dct_names[number] = initial_list[3:-1]

    # print(dct_names)

    for number, names in dct_names.items():
        str_ = ''
        for part in names:
            str_ += part + ' '
        dct_names[number] = str_

    # print(dct_names)

    top250_ready = open('top250_movies_ready.txt', 'a')
    for number, title in dct_names.items():
        top250_ready.write("{:>3}".format(str(number)) + ' ' + title + '\n')
    top250_ready.close()

    # ratings
    # ratings dictionary
    dct_ratings = {}
    for number, initial_list in dct.items():
        for index, element in enumerate(initial_list):
            if index == 2:
                dct_ratings[number] = float(element)

    # print(dct_ratings)

    # to re-execute the program
    ratings = open('ratings.txt', 'w')
    ratings.close()

    # histogram formation
    ratings = open('ratings.txt', 'a')
    for number, rating in dct_ratings.items():
        stars = "{:>3}".format(str(number)) + ' '\
                + '*' * int(rating * 10) + '\n'
        # stars = str(str(number) + ' ' + '*' * (int(rating) * 10) + '\n')
        ratings.write(stars)
    ratings.close()

    # years
    # years dictionary
    dct_years = {}
    for number, initial_list in dct.items():
        for index, element in enumerate(initial_list):
            if element == initial_list[-1]:
                element = element.strip('(')
                element = element.strip(')')
                element = element.rstrip('/I')
                dct_years[number] = element

    # print(dct_years)

    # to re-execute the program
    years = open('years.txt', 'w')
    years.close()

    # histogram formation
    years = open('years.txt', 'a')
    for number, year in dct_years.items():
        # T - 1000 years, C - 100 years, D - 10 years, O - 1 year
        T = int(year) // 1000
        C = (int(year) % 1000) // 100
        D = ((int(year) % 1000) % 100) // 10
        Oo = ((int(year) % 1000) % 100) % 10
        letters = "{:>3}".format(str(number)) + ' ' + 'T' * T + 'C' * C\
                  + 'D' * D + 'O' * Oo + '\n'
        years.write(letters)
    years.close()

    # to re-execute the program
    if os.path.exists('top250_movies.txt'):
        os.remove('top250_movies.txt')
    os.rename('top250_movies_ready.txt', 'top250_movies.txt')

except IOError:
    print("An error occurred while opening the file!")
except ValueError:
    print("Error!")
