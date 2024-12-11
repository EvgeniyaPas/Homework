import threading
import time
from queue import Queue
import random


class Table:
    guest = None
    def __init__(self, number):
        self.number = number


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep_time = random.uniform(3, 10)
        time.sleep(sleep_time)


class Cafe(Table, Guest):
    def __init__(self, queue, *tables):
        self.queue = queue
        self.tables = tables

    def guest_arrival(self, *guests):  # прибытие гостей
        for i in guests:
            if Table.guest is None:
                Table.guest = i
                print(i, 'сел(-а) за стол номер', 1)
            else:
                self.queue = Queue()
                self.queue.put(i)
                print(i, 'в очереди')

    def discuss_guests(self):   # обслужить гостей
        while not self.queue.empty():
            if Guest.is_alive():
                print(self.name)
                Table.guest = None



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
#cafe.discuss_guests()






