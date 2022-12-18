from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import pytest
import unittest
from pytest_bdd import scenario, given, when, then
from math import *

#TDD_1
def test_rect():
    s = Rectangle("синего", 1, 2)
    assert 1*2 == s.square()

def test_circ():
 # должен выдать ошибку
    c = Circle("зеленого", 2)
    assert pi*(2**2) == c.square()

def test_sq():
    c = Square("красного", 4)
    assert 4*4 == c.square()


#TDD_2
class TestFigure(unittest.TestCase):
    def test_rect(self):
        self.assertEqual(Rectangle("синего", 1, 2).square(), 2)


#BDD
@scenario('feature.feature', 'Print characterictics of the figure')
def test1():
    print('Scenarios: Characterictics of the figure')

@given("I was given a figure")
def test2():
    print("\nI was given a figure")
    print(f"Figure: {Rectangle('синего', 1, 2)}\n")

@when('I checked functions')
def test3():
    r = Rectangle('синего', 1, 2)
    if r.square() == 2:
        print("All correct")

@then('I print characterictics of the figure')
def test4():
    print('I print characterictics of the figure')
    r = Rectangle('синего', 1, 2)
    print(r)

if __name__ == "__main__":
    unittest.main()