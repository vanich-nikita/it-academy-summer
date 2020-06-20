"""
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.
Входные данные.
Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
Пример:
3 - N количество школьников
2 - M1 количество языков первого школьника
Russian - языки первого школьника
English
3 - M2 количество языков второго школьника
Russian
Belarusian
English
3 - M3 количество языков третьего школьника
Russian
Italian
French
Выходные данные
В первой строке выведите количество языков,
которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
"""


def input_data():
    # dictionary for data storage
    dct = {}
    # for key of dictionary
    n = 1

    N = int(input("Input number of students: "))

    while N > 0:
        M = int(input("Input number of languages: "))
        # language storage list
        lang = []
        while M > 0:
            lng = input("Input languages: ")
            # adding data to the dictionary
            lang.append(lng)
            # dictionary formation
            dct[n] = lang
            # to prevent endless loop
            M -= 1
        # to prevent endless loop
        N -= 1
        # key increase
        n += 1
    return dct


def output_data(dct):
    sets = []
    for i in dct.values():
        sets.append(set(i))
    # for test
    # print(sets)

    # another way of intersection sets (for test)
    # common_languages = set.intersection(*[set(contract)
    # for contract in sets])
    common_languages = set.intersection(*map(set, sets))
    # comment output
    # print("The number of common\
# languages: {0}".format(len(common_languages)))
    # output without comment
    print(len(common_languages))
    # comment output
    # print("The common languages: ", *common_languages, sep='\n')
    # output without comment
    print(*common_languages, sep='\n')
    at_least_one_student_knows = set.union(*map(set, sets))
    # comment output
    # print("The number of languages that at least one student knows:\
# at least one of: {0}"\
    # .format(len(at_least_one_student_knows)))
    print(len(at_least_one_student_knows))
    # comment output
    # print("The languages that at least one student knows: ",\
    #      *at_least_one_student_knows, sep='\n')
    print(*at_least_one_student_knows, sep='\n')


x = input_data()
# for test
# print(x)
# for test
# print(len(x))
output_data(x)
