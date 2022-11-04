from lab_python_fp.field import field, main1
from lab_python_fp.gen_random import gen_random, main2
from lab_python_fp.unique import Unique, main3
from lab_python_fp.sort import result, main4
from lab_python_fp.sort import result_with_lambda
from lab_python_fp.print_result import test_1, test_2, test_3, test_4, main5
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2, main6
from lab_python_fp.process_data import f1, f2, f3, f4, main7
import time
import json
import sys


with open('C:\\Users\\dasha\\data_light.json', encoding="utf8") as f:
    data = json.load(f)

def main():
    print()


    #__________f1________________
    # for i in Unique(field(data, 'job-name')):
    #     print(i)
    # @print_result
    # sorted(Unique(field(data, 'job-name')))
    #print(f1(data))
    #f2(f1(data))
    #f3(f2(f1(data)))
    # with cm_timer_1():
    #     f4(f3(f2(f1(data))))
    # for i in Unique(field(data, 'job-name'), ignore_case=True):
    #     print(i)


    #main1()
    #main2()
    #main3()
    #main4()
    #main5()
    #main6()
    main7()

if __name__ == '__main__':
    main()


