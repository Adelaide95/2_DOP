#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Дано натуральное число.
Определить, будет ли это число: нечётным, кратным 5
Хацукова Аделаида
"""
if __name__ == '__main__':
    A = int(input("Введите натуральное число: "))
    if A % 2 == 1:
        if A % 5 == 0:
            print("Число кратно 5")
        print("Число нечетное")
    else:
        print("Число четное и не кратно 5")
