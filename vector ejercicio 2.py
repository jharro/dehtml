#2.	Elabore un subprograma que calcule y retorne la suma de los datos múltiplos de 3 de un vector de n elementos.

#Subprograma

import Vector as vector 

n = int(input("Digite el tamaño del vector: \n"))
miVector=[]
vector.LlenarVector(miVector,n)
suma = vector.SumaDatos(miVector,n)
promedio = vector.promedioVector(suma,n)
print(miVector)
print(promedio)

print("\n----------------------------------------------------------\n")

