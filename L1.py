import sys
import math




# Проверка на корректность ввода числа
def corr_coef(coef_str):
    f = 1
    s = '0123456789.'
    if coef_str[0]=='-':
        coef_str=coef_str[1:]
    for i in range(len(coef_str)):
        if coef_str[i] not in s:
            return False
    if coef_str.count('.') > 1:
        return False
    return True




def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()

    # Переводим строку в действительное число
    if corr_coef(coef_str):
        coef = float(coef_str)
        return coef
    else:
        while corr_coef(coef_str)!=True:
            try:
                # Пробуем прочитать коэффициент из командной строки
                coef_str = sys.argv[index]
            except:
                # Вводим с клавиатуры
                print(prompt)
                coef_str = input()
        coef = float(coef_str)
        return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1>=0:
            root11=math.sqrt(root1)
            root12=-math.sqrt(root1)
            if root12==root11:
                result.append(root11)
            else:
                result.append(root11)
                result.append(root12)
        if root2 >= 0:
            root21 = math.sqrt(root2)
            root22 =-math.sqrt(root2)
            if root21 == root22:
                result.append(root22)
            else:
                result.append(root21)
                result.append(root22)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')



    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots ==4:
        print('Четыре корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
