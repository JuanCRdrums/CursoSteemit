#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = input("Ingresa un número: ")
    par = False
    tres = False
    if n % 2 == 0:
        par = True
    if n % 3 == 0:
        tres = True

    if par and tres:
        print n, " es un número par y un múltiplo de 3."
    elif par:
        print n, " es un número par."
    elif tres:
        print n, " es un múltiplo de 3."
    else:
        print n, " no es un número par ni un múltiplo de 3."
