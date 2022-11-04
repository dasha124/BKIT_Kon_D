import time
from contextlib import contextmanager
class cm_timer_1():
    def __int__(self):
        pass
    def __enter__(self): # создание и возвращение объкта базы данных
        print("cm_timer_1 -> time_1")
        self.time1 = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb): # закрытие подключения
        print("cm_timer_1 -> time_2")
        self.time2 = time.time()
        t = self.time2-self.time1
        print(t)

# Yield — это ключевое слово в Python,
# которое используется для возврата из функции с сохранением состояния ее локальных переменных,
# и при повторном вызове такой функции выполнение продолжается с оператора yield,
# на котором ее работа была прервана.
@contextmanager
def cm_timer_2():
    print("cm_timer_2 -> time_1")
    t1 = time.time()
    yield
    print("cm_timer_2 -> time_2")
    t2 = time.time()
    t = t2-t1
    print(t)

def main6():
    with cm_timer_1():
         time.sleep(5.5)
    print('//-----------------------//')
    with cm_timer_2():
        time.sleep(5.5)


if __name__ == '__main__':
    main6()
