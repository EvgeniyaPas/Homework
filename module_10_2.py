import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        kol_voinov = 100
        counter = 0
        while kol_voinov != 0:
            kol_voinov -= self.power
            counter += 1
            print(f'{self.name} сражается {counter} день(дня)..., осталось {kol_voinov}\n', end = '')
            time.sleep(1)
        print(f'{self.name}, одержал победу спустя {counter} дней(дня)!\n', end = '')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
