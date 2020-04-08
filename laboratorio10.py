# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:54:42 2020

@author: Carlos CJ
"""
def a_power_b(a,b):
    Potencia = a
    if b == 1 :
        print("la potencia es  ", str(Potencia))
    else :
        for r in range(2,(b+1)):
            Potencia = (Potencia * a)
        print("la potencia es  ", str(Potencia))
a = int(input("Ingrese el valor del numero que va en a"))
b = int(input("Ingrese el valor del numero que va en b"))
print(a_power_b(a,b))