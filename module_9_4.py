from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        return choice(self.words)

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda first, second: first[0] == second[0], first, second))
print(list(result))

def get_advanced_writer(file_name):
    def write_everything(*data_set):

        with open(file_name, 'a', encoding = 'utf-8') as file:
            for i in data_set:
                file.write(f'{i}\n')
            return file_name

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Ваш класс здесь
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


