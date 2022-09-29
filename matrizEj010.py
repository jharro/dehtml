filas=int(input("Filas: "))
while filas<=0:
    filas=int(input("El número de filas debe ser mayor a 0: "))

#print("Usted dijo ",filas," filas para la matriz")

columnas=int(input("Columnas: "))
while columnas<=0:
    columnas=int(input("El número de columnas debe ser mayor a 0: "))

#print("Usted dijo ",columnas," columnas para la matriz")
    
print("La matriz tendrá una dimensión de :",filas, " filas * ",columnas," columnas ")

#Ingrese de datos
print("\nIngreso de datos")
matriz=[]
for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            valor=float(input("Fila {}, Columna {} : ".format(i+1, j+1)))
            matriz[i].append(valor)

#Mostrar el contenido de la matriz
for f in range(filas):#0 1 2 
   
    for c in range(columnas):# 0 1 2 
        print(matriz[f][c],end=' ') 
       
    print("\n")
  


#suma de cada fila
for f in range(filas):
    sumaFila=0
    for c in range(columnas):
        
        sumaFila+=matriz[f][c]
    print("\n")
    print("La suma de la fila ",f," es: ",sumaFila)

#validar si la matriz es cuadrada
sumaDiagonal=0
if filas==columnas:
    print("La matriz es cuadrada")
    for f in range(filas):
        for c in range(columnas):
            if f==c:
                sumaDiagonal+=matriz[f][c]
else:
    print("La matriz NO es cuadrada...")
    
print("\nLa suma de los elementos de la diagonal principal es: ", sumaDiagonal)  