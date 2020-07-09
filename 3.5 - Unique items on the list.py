"""
Дан список. Выведите те его элементы, которые встречаются в списке
только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""

lst = [1, 1, 2, 3, 3, 4, 4, 1, 0, 6, 7, 11]
# final_list = []
#
# for i in lst:
#     if lst.count(i) == 1:
#         final_list.append(i)
# print(final_list)


def single_element(list_, result):
    if len(list_) == 0:
        return result
    if list_[0] in list_[1:]:
        return single_element([x for x in list_[1:] if x != list_[0]], result)
    else:
        return single_element(list_[1:], result + [list_[0]])


print(single_element(lst, []))
