import json
import sys
import time
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.sort import result
from lab_python_fp.sort import result_with_lambda
from lab_python_fp.print_result import test_1, test_2, test_3, test_4, print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.cm_timer import cm_timer_2



with open('C:\\Users\\dasha\\data_light.json', encoding="utf8") as f:
    data = json.load(f)

#@print_result
def f1(arg) -> list:
    return sorted(Unique(field(data, 'job-name'), ignore_case=True))

#@print_result
def f2(arg) -> list:
    #return list(filter(lambda s: s[0:len('программист')]=='Программист', sorted(Unique(field(data, 'job-name'), ignore_case=True))))
    return list(filter(lambda s: s[0:len('программист')]=='Программист', arg))

#@print_result
def f3(arg) ->list:
    return list(map(lambda s: s+' с опытом работы Python', arg))

@print_result
def f4(arg)->list:
    return list(zip(arg, ['зарплата '+str(s)+' руб.' for s in gen_random(len(arg), 100000, 200000)]))


def main7():
    with cm_timer_1():
        f4(f3(f2(f1(data))))

if __name__ == '__main__':
    main7()