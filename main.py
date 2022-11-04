from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import emoji




def main():
    print()
    r = Rectangle("синего", 8, 8)
    c = Circle("зеленого", 8)
    s = Square("красного", 8)
    print(r)
    print(c)
    print(s)
    print("Работа с виртуальным окружением и pip")

    print(emoji.emojize('Python is :thumbs_up:'))

if __name__ == "__main__":
    main()