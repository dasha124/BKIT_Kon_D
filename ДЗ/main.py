
# последовательность Рекамана

def rec():
    n = 0
    prev, cur = 0, 0
    l = []
    while True:
        if n>0 and (prev - n)>0 and (prev - n) not in l:
            cur = prev - n
            yield cur
        else:
            cur = prev + n
            yield cur
        l.append(cur)
        prev = cur
        n += 1

if __name__ == '__main__':
    rec_gen = rec()
    for i in range(10):
        j = next(rec_gen)
        print(j)
