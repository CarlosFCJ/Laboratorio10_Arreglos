# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:54:42 2020

@author: Carlos CJ
"""
# La funcion a_power_b sirve para realizar una potencia sin utilizar math ni **
def a_power_b(a,b):
    Potencia = a
    if b == 1 :
        Potencia = a
    else :
        for r in range(2,(b+1)):
            Potencia = (Potencia * a)
    return Potencia
# La funcion bucle ejecuta tantas veces como la persona lo dese la funcion a_power_b actualizando 
# siempre los numeros hasta que el dijite que a es igual a 0
# Luego impre cuantas potencias se calcularon y cuantos resultados fueron impares y pares
def bucle():
    a = 1
    c = 0
    Par = 0
    Impar = 0
    while a != 0 :
        a = int(input("Ingrese el valor del numero que va en a :"))
        b = int(input("Ingrese el valor del numero que va en b :"))
        if a != 0 :
            Com = a_power_b(a,b)
            print("La potencian es " + str(Com))
            c = c+1
            if (Com%2) == 0 :
                Par = Par + 1
            else :
                Impar = Impar +1
    print("El numero potencias calculadas es " + str(c))
    print("El numero de resultados pares fue " + str(Par))
    print("El numero de resultados impares fue " + str(Impar))
    print("termino")
print(bucle())