"""
Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов
или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""

str_ = open('ReadMe.txt', 'r', encoding='utf8')
a = str(str_.read())
# for test
# print(str_.read())
final_str = []
# for test
# print(set(a.split()))
for i in set(a.split()):
    if i.isalpha():
        final_str.append(i)
print(set(final_str))
print(len(set(final_str)))
str_.close()
# for test
# print(final_str)
