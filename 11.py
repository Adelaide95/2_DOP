#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Имеются две ёмкости: кубическая с ребром A, цилиндрическая с высотой H и радиусом основания R.
Определить, поместится ли жидкость объёма M в первую ёмкость, во вторую, в обе.
Хацукова Аделаида
"""

import math
if __name__ == '__main__':
    A = float(input("Ребро кубла равно: "))
    H = float(input("Высота цилиндра равна: "))
    R = float(input("Радиус основания цилиндра равен: "))
    M = float(input("Объем жидкости: "))

    V = A**3
    Vh = math.pi * R * R * H
    if V >= M and Vh >= M:
        print("Жидкость заданного объема поместиться в обе емкости")
    elif V >= M and Vh < M:
        print("Жидкость заданного объема поместиться в первую емкость")
    elif V < M and Vh >= M:
        print("Жидкость заданного объема поместиться во вторую емкость")
    else:
        print("Жидкость заданного объема не поместиться ни в одну из емкостей")


