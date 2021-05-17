#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(1, 2, 3, 4, 5)
    r1.display()

    print("---")

    r1 = Rectangle(1, 2)
    r1.display()
