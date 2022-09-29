#Subprograma para llenar la lista

import random as aleatorio
def LlenarVector(vector,n):
    
    for i in range(n):
        valor=aleatorio.randrange(0,n+100)
        vector.append(valor)
 
def ImprimirPosImpares(vector,n):
    for i in range(n):
        if i % 2 !=0:
            print(vector[i])       

def SumaDatos(v,n):
    suma = 0
    for i in range(n):
        suma = suma + v[i]
    return suma

def promedioVector(s,n):
    promedio = 0
    promedio = s/n
    return s
    
#Algoritmo principal
# n=int(input("Ingrese el tamaño del vector: "))
# miLista=[]
# LlenarVector(miLista,n)
# ImprimirPosImpares(miLista,n)

