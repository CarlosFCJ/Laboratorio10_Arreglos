# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:54:42 2020

@author: Carlos CJ
"""
# La funcion a_power_b sirve para realizar una potencia sin utilizar math ni **
def a_power_b(a,b):
    Potencia = a
    if b == 1 :
        print("la potencia es  ", str(Potencia))
    else :
        for r in range(2,(b+1)):
            Potencia = (Potencia * a)
        print("la potencia es  ", str(Potencia))
def bucle():
    a = 1
    while a != 0 :
        a = int(input("Ingrese el valor del numero que va en a :"))
        b = int(input("Ingrese el valor del numero que va en b :"))
        print(a_power_b(a,b))
    print("termino")
print(bucle())