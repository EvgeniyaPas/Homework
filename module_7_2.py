import io
from pprint import pprint

def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding = 'utf-8')
    keys = []
    values = []
    number_of_string = 1
    for i in strings:
        keys.append((number_of_string, file.tell()))
        file.write(f'{i}\n')
        values.append(i)
        number_of_string += 1

    strings_positions = dict(zip(keys, values))
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
