#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Дано вещественное число.
Определить, какое это число: положительное, отрицательное, ноль.
Хацукова Аделаида
"""

if __name__ == '__main__':
    A = float(input("Введите вещественное число: "))
    if A > 0:
        print("Число положительное")
    elif A < 0:
        print("Число отрицательное")
    else:
        print("Число равно нулю")