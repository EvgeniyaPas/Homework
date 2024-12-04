from datetime import datetime
from threading import Thread
import time
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        time.sleep(0.1)
        file.write(f'Какое-то слово № {word_count}')
    print("Завершилась запись в файл", file_name)

time_1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_2 = datetime.now()
# время работы потоков
print('Paбота потоков', time_2 - time_1)
time_3 = datetime.now()
th = Thread(target=write_words(10, 'example5.txt'))
th = Thread(target=write_words(30, 'example6.txt'))
th = Thread(target=write_words(200, 'example7.txt'))
th = Thread(target=write_words(100, 'example8.txt'))
time_4 = datetime.now()
th.start()
th.join()
time_4 = datetime.now()
print('Paбота потоков', time_4 - time_3)
