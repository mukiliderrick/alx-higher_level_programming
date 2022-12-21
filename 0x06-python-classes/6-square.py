#!/usr/bin/python3
def area(self):
    return self.__size ** 2

def my_print(self):
    if self.__size == 0:
        print()
    else:
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
