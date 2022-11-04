def print_result(func):
    def wrapper(l=[], *args, **kwargs):
    #def wrapper():
        #print("FunctionName =", func.__name__)
        res = func(l, *args, **kwargs)
        #res = func()
        print("type =", type(res))
        if type(res) is list:
            print(*res, sep='\n')
        elif type(res) is dict:
            for key in res:
                print(key, "=", res[key])
        return res
    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


def main5():

    test_1()
    test_2()
    test_3()
    test_4()

if __name__ == '__main__':
    main5()