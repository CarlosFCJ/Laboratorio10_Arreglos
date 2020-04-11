# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 09:54:42 2020

@author: Carlos CJ
"""
import numpy as np
# La funcion a_power_b sirve para realizar una potencia sin utilizar math ni **
def a_power_b(a,b):
    Potencia = a
    if b == 1 :
        Potencia = a
    else :    
        if b%2 != 0 :
            f = b//2
            x = b-(f*2)
            b = b-x
            Potencia = Potencia + (a*x)
            b = int(b)
        for r in range(2,(b+1)):
            Potencia = (Potencia * a)
    return Potencia
#La funcion mean_arreglos sirve para calcular promedios
def mean_arreglos(l,Numero):
    c = 0
    n = 0
    p = Numero
    t = l
    while n<p :
        c = c + t[n]
        n = n +1
    Promedio = c/p
    return Promedio
# La siguiente funcion sirve para calcular seviaciones standar, mediante el promedio, un contador,
# una lista y el numero de datos de la lista
def std_arreglo(ls,pro,Nu):
    d = 0
    for t in range(0,Nu):
        d = d + ((ls[t]-pro)**2)
    de = d/(Nu-1)
    std = (de**(1/2))
    return std
#La funcion norm_arreglos normalisa los datos de cada arreglo restandole su promedio y luego 
#dividiendolo en el estandar, n sirve para saber el numero de datos de la lista y ls para 
# Tener los datos dentro de la lista
def norm_arreglos(ls,st,pro,N):
    f = []
    for g in range(0,N):
        nor = (ls[g]-pro)/st
        f.append(nor)
    return f
# La funcion bucle ejecuta tantas veces como la persona desea al haber ingresado el numero al inicio
# Luego impre cuantas potencias se calcularon y cuantos resultados fueron impares y pares
def bucle(Numero):
    a = 1
    c = 0
    ct = 0
    Par = 0
    Impar = 0
    #La lista que se utilizaran para guardar los datos
    lisA = []
    lisB = []
    while ct < Numero :
        a = int(input("Ingrese el valor del numero que va en a :"))
        #Usando append se guarda el nuevo dato en la lista
        lisA.append(a)
        print(lisA)
        b = int(input("Ingrese el valor del numero que va en b :"))
        #Usando append se guarda el nuevo dato en la lista
        lisB.append(b)
        print(lisB)
        if a != 0 :
            Com = a_power_b(a,b)
            print("La potencian es " + str(Com))
            c = c+1
            if (Com%2) == 0 :
                Par = Par + 1
            else :
                Impar = Impar +1
            ct = ct + 1
    print("El numero potencias calculadas es " + str(c))
    print("El numero de resultados pares fue " + str(Par))
    print("El numero de resultados impares fue " + str(Impar))
    print("termino")
    #Se crean los arreglos usando las listas
    listaA = np.array(lisA)
    listaB = np.array(lisB)
    l = lisA
    ProA = mean_arreglos(l,Numero)
    print("El promedio de las a fue :",ProA)
    l = lisB
    ProB = mean_arreglos(l,Numero)
    print("El promedio de las b fue :",ProB)
    proab = a_power_b(ProA,ProB)
    print("La potencia de a promedio y b promedio fue ", str(proab))
    destA = std_arreglo(listaA,ProA,Numero)
    destB = std_arreglo(listaB,ProB,Numero)
    print("La deviacion standar de A es :" + str(destA))
    print("La deviacion standar de B es :" + str(destB))
    listaAN = np.array(norm_arreglos(listaA,destA,ProA,Numero))
    listaBN = np.array(norm_arreglos(listaB,destB,ProB,Numero))
    print("La lista antes de la normalizar ")
    print(listaA)
    print("La lista de A despues de Normalizarla")
    print(listaAN)
    print("La lista antes de la normalizar ")
    print(listaB)
    print("La lista de B despues de Normalizarla")
    print(listaBN)
    NProA = mean_arreglos(listaAN, Numero)
    print("El promedio normalizado es :" + str(NProA))
    destAN = std_arreglo(listaAN,NProA,Numero)
    print("la nueva deviacion estandar es :"+ str(destAN))
    NProB = mean_arreglos(listaBN, Numero)
    print("El promedio normalizado es :" + str(NProB))
    destBN = std_arreglo(listaBN,NProB,Numero)
    print("la nueva deviacion estandar es :"+ str(destBN))
Numero = int(input("Ingrese el numero de potencias que va a calcular :"))
bucle(Numero)