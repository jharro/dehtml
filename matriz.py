'''
10  23  21
61  100 2
12  75  17

ok - Cantidad de valores mayores a 60 ---> 1 : contador ->función
ok - Suma de los valores entre 60 y 100---> 236 : sumar acumulador->función
0k-Cantidad de valores entre 60 y 100---> 3 : contador->función

Entero CanVa60_100(M, fila, columna)
CanVa60_100: Entero
CanVa60_100=0

INICIO
Para i =0 hasta fila
      Para j=0 hasta columna
          Si M[i,j] >= 60 y M[i,j] <= 100 Entonces
              CanVa60_100 = CanVa60_100 + 1
          FinSi
      Fin(Para)
    Fin(Para)
retorne(CanVa60_100)
FIN



MATRICES
Entero sumaValores60_100(M,fila,columna)
sumaVa60_100:Entero
sumaVa60_100=0
INICIO
Para i =0 hasta fila
      Para j=0 hasta columna
          Si M[i,j] >= 60 y M[i,j] <= 100 Entonces
              sumaVa60_100 = sumaVa60_100 + M[i,j]
          FinSi
      Fin(Para)
    Fin(Para)
retorne(sumaVa60_100)
FIN

Entero mayorSesenta(M,fila,columna)
  contador60:Entero
  contador60=0
  INICIO
    Para i =0 hasta fila
      Para j=0 hasta columna
          Si M[i,j] > 60 Entonces
              contador60 = contador60 + 1
          FinSi
      Fin(Para)
    Fin(Para)
    retorne(contador60)
  FIN  
  

void llenaMatriz(M,fila,columna)
INICIO
   Para i=0 hasta fila
      Para j=0 hasta columna
         LEA M[i,j]
      Fin(Para)
   Fin(Para)
FIN   

void imprimirMatriz(M,fila,columna)
INICIO
   Para i=0 hasta fila
      Para j=0 hasta columna
         Escribir(M[i,j])
      Fin(Para)
   Fin(Para)
FIN

Algoritmo Matrices
   miMatriz[filas,columnas] : Numérico
   filas,columnas:Numérico
   resultadoMayorSesenta,sumava60_100:numérico
   sumava60_100=0
   canVa60_100:Entero
   
   INICIO
     LEA filas   -----------> 4
     LEA columnas-----------> 3
     llenaMatriz(miMatriz,filas,columnas)
     imprimirMatriz(miMatriz,filas,columnas)
     resultadoMayorSesenta= mayorSesenta(miMatriz,filas,columnas)
     Escribir(resultadoMayorSesenta)
     sumava60_100=sumaValores60_100(miMatriz,fila,columna)
     Escribir(sumava60_100)
     canVa60_100=CanVa60_100(miMatriz, fila, columna)
     Escribir(canVa60_100)
     
   FIN
Fin Algoritmo
     
      

'''
def imprimir(m,f,c):
    filas=len(m)
    columnas=len(m[0])
    print("\n")
    for i in range(filas):
        for j in range(columnas):
            print(m[i][j],sep=',',end=' ')
        print("\n")#Deja sun salto de línea entre cada fila

def llenarMatriz(m,f,c):
    for f in range(filas):
        matriz.append([])
        print("Fila: ",f)
        for c in range(columnas):
            print("Columna: ",c)
            valor=int(input("Valor: ")) #leer
            matriz[f].append(valor)
'''
10 , 20  15

25  1   4

18  5   10  
'''
#Programa principal

matriz=[] # una lista vacía
filas=int(input("Cuántas filas? "))
columnas=int(input("Cuántas columnas? "))

llenarMatriz(matriz,filas,columnas)
  
imprimir(matriz,filas,columnas)