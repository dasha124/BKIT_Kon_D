import random
def gen_random(num_count, begin, end):
    l = [random.randint(begin, end) for _ in range(num_count)]
    return l

def main2():

    print(gen_random(5, 3, 10))

if __name__ == '__main__':
    main2()