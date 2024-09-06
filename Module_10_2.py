import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.warrior = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.warrior > 0:
            time.sleep(1)
            self.days += 1
            self.warrior -= self.power
            print(f'{self.name} сражается {self.days} дней, осталось {self.warrior} воинов')
            if self.warrior < 0:
                self.warrior = 0
        print(f'{self.name} одержал победу спустя {self.days} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
