import pytest
import unittest
from main import rec
#TDD

def test_1():
    rec_gen = rec()
    l = []
    for i in range(10):
        l.append(next(rec_gen))
    assert [0, 1, 3, 6, 2, 7, 13, 20, 12, 21] == l


def test_2():
    rec_gen = rec()
    assert 1 == rec_gen(1)

def test_3():
    rec_gen = rec()
    l = []
    for i in range(11):
        l.append(next(rec_gen))
    assert 11 == l[-1]


if __name__ == "__main__":

    unittest.main()