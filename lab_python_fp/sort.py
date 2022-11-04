def result(data):
    return sorted(data, key=abs, reverse=True)

def result_with_lambda(data):
    return sorted(data, key=lambda i: abs(i), reverse=True)


data4 = [4, -30, 100, -100, 123, 1, 0, -1, -4]
def main4():

    print(result(data4))
    print(result_with_lambda(data4))

if __name__ == '__main__':
    main4()