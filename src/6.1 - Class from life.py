"""
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ. Создайте несколько
объектов классов, которые описывают ситуацию Объекты должны содержать
как атрибуты так и методы класса для симуляции различных действий.
Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию
- вызывать методы, взаимодействие объектов и т.д.
В данной программе создадим небольшую викторину.
"""


class Question:
    """Класс, определяющий типовой вопрос """

    def __init__(self, question, answer1, answer2,
                 answer3, answer4, solution):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__solution = solution

    # Сеттеры и геттеры
    def set_question(self, question):
        self.__question = question

    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_solution(self, solution):
        self.__solution = solution

    def get_question(self):
        return self.__question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_solution(self):
        return self.__solution

    def __str__(self):
        """Выводит вопросы"""
        result = self.get_question() + '\n' + \
                 '1. ' + self.get_answer1() + '\n' + \
                 '2. ' + self.get_answer2() + '\n' + \
                 '3. ' + self.get_answer3() + '\n' + \
                 '4. ' + self.get_answer4()
        return result

    def isCorrect(self, answer):
        """Проверяет ответ"""
        return answer == self.get_solution()


def congratulate(point):
    """Выводит конечный результат и поздравляет игрока"""
    if point <= 4:
        print("Вы заработали", point, "очков. Не расстраивайтесь - Ваши"
                                      " знания нахдятся на базовом уровне"
                                      " но требуют дальнейшего улучшения!")
    elif (point > 4) and (point <= 8):
        print("Вы заработали", point, "очков. Поздравляем!"
                                      " Ваши знания находятся на"
                                      " достаточно высоком уровне!")
    else:
        print('Вы заработали', point, 'очков. Вы просто супер!')


def main():
    """Главная функция"""
    points = 0

    # Создание списка вопросов.
    questions = get_questions()

    for i in range(10):

        current = questions[i]
        print(current)
        user_answer = int(input("Введите ваше решение (номер"
                                " между 1 и 4): "))
        if current.isCorrect(user_answer):
            points += 1
            print("Это правильный ответ.")
            print()
        else:
            print("Неправильно. Правильный ответ",
                  current.get_solution())
            print()

    congratulate(points)


def get_questions():
    """Создает перечень вопросов и добавляет их в список."""

    questions = []

    question1 = Question("Сколько дней в лунном году?",
                         "354", "365", "243", "379", 1)
    questions.append(question1)
    question2 = Question("Какая самая большая планета?", "Марс", "Юпитер",
                         "Земля", "Плутон", 2)
    questions.append(question2)
    question3 = Question("Какой кит самый большой?",
                         "Косатка",
                         "Горбатый кит",
                         "Белуга", "Синий кит", 4)
    questions.append(question3)
    question4 = Question("Какой динозавр мог летать?",
                         "Трицератопс", "Тираннозавр",
                         "Птеранодон", "Диплодок", 3)
    questions.append(question4)
    question5 = Question("Какие планеты солнечной системы вращаются"
                         "в направлении, противоположном Земле?",
                         "Венера и Уран", "Юпитер и Нептун",
                         "Меркурий и Марс", "Плутон и Уран", 1)
    questions.append(question5)
    question6 = Question("Какая из них самая жаркая планета?",
                         "Марс", "Плутон", "Земля",
                         "Венера", 4)
    questions.append(question6)
    question7 = Question("У какого животного самый большой мозг"
                         "по отношению к телу?",
                         "Дельфин",
                         "Слон",
                         "Муравей", "Шимпанзе", 3)
    questions.append(question7)
    question8 = Question("Какой из пингвинов самый крупный?",
                         "Антарктический пингвин",
                         "Золотоволосый пингвин",
                         "Императорский пингвин",
                         "Белокрылый пингвин", 3)
    questions.append(question8)
    question9 = Question('Что в переводе с греческого означает "комета"',
                         "Быстрое тело",
                         "Хвостатая звезда",
                         "Пришелец",
                         "Разрушитель", 2)
    questions.append(question9)
    question10 = Question("Сколько длится год на Марсе?",
                          "550 земных дней", "498 земных дней",
                          "126 земных дней", "687 земных дней", 4)
    questions.append(question10)

    return questions


# Вызов главной функции.
if __name__ == '__main__':
    main()
