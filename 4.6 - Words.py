"""
Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов
или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""


str_ = open('ReadMe.txt', 'r', encoding='utf8')
input_text = str(str_.read())
final_str = set(input_text.split())
print("The input text: has {} different words"
      .format(len(final_str)))
str_.close()
