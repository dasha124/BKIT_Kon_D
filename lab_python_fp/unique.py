# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        # По-умолчанию ignore_case = False -> Aбв и АБВ - одинаковые строки
        #print('len(kwargs) =', len(kwargs))
        len1 = len(kwargs)
        global Ff
        if len1==0:
            Ff = False
        else:
            for key in kwargs:
                Ff = kwargs[key]
        self.used_elements = set()
        self.data = items
        self.index = 0

    def __iter__(self):
        # метод __iter__() – "превращать" итерируемый объект в итератор.
        # Если в цикл for передается уже итератор, то метод __iter__() этого объекта должен возвращать сам объект
        return self


    def __next__(self): #выдачa очередного элемента
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                #print("!!!!!!!!!!!!!!!")
                if current not in self.used_elements:
                    if Ff==False:
                        #print("CHECK", current, "-", current.lower())
                        if type(current) is not int:
                            if current.lower() not in self.used_elements:
                                self.used_elements.add(current.lower())
                                return current
                        else:
                            if current not in self.used_elements:
                                self.used_elements.add(current)
                                return current
                    else:
                        self.used_elements.add(current)
                        return current

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = ['a', 'A', 'b', 'B', 'A', 'Abc', 'AbC']

def main3():
    for i in Unique(data1):
        print(i)
    print('//-------------------//')
    for i in Unique(data2):
        print(i)
    print('//-------------------//')
    for i in Unique(data2, ignore_case=True):
        print(i)

if __name__ == '__main__':
    main3()
