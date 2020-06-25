"""
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию,
которая этот список “сворачивает”
get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
get_ranges([4,7,10]) // "4,7,10"
get_ranges([2, 3, 8, 9]) // "2-3,8-9"
"""


def get_ranges(lst):
    str_ = ''
    left_border = 1
    for num, elem in enumerate(lst):
        if len(lst) == 1:
            print(lst[0])
            break
        for next_elem in lst[left_border:]:
            # checking initial values
            if num == 0 and next_elem - elem != 1:
                str_ += str(elem) + ','
                if next_elem == lst[-1] and str(next_elem) not in str_:
                    str_ += str(next_elem)
                break
            if num == 0 and next_elem - elem == 1:
                str_ += str(elem) + '-'

            if num == 1 and next_elem - elem == 1 and '-' not in str_:
                str_ += str(elem) + '-'

            # checking the difference of neighboring elements in 1
            if next_elem - elem == 1 and next_elem != lst[-1]:
                if str_[-1] != '-':
                    str_ += '-'
                break

            if next_elem - elem == 1 and next_elem == lst[-1] \
                    and str_[-1] == str(elem):
                str_ += '-' + str(next_elem)
                break

            if next_elem - elem == 1 and next_elem == lst[-1]:
                str_ += str(next_elem)

            # checking the difference of neighboring elements more than 1
            if next_elem - elem != 1:
                if str(elem) in str_:
                    str_ += ','
                    if str(next_elem) not in str_:
                        str_ += str(next_elem)
                        break
                else:
                    str_ += str(elem) + ',' + str(next_elem)

                if str(next_elem) in str_:
                    break
                if str(next_elem) == lst[-1]:
                    str_ += str(elem) + ',' + str(next_elem)
        left_border += 1
    print(str_)


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([1, 4, 7, 10, 15])
get_ranges([2, 3, 8, 9])
get_ranges([0, 2, 3, 8, 9])
get_ranges([0, 1, 3, 4, 8, 9])
get_ranges([0, 3, 5, 6, 8, 9, 11])
get_ranges([0, 1, 3, 5, 7, 9, 10, 11])
get_ranges([0, 5])
get_ranges([0])
