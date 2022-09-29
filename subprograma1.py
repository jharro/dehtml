'''
1.	Escriba el algoritmo que lea un valor entero n y que haga lo siguiente:
determine si el número es par o impar, imprima todos los números desde 1 hasta n,
y que halle la suma desde 1 hasta n.
'''
'''
#Procedimiento tipo void
void ParImpar(numero)
INICIO
  Si numero mod 2 = 0 entonces
     Escriba "Es par"
  Sino
     Escriba "Es impar"
  FinSi
FIN       
  
  
#Algoritmo ppal
numero:entero
INICIO
 LEA numero ---6 
 ParImpar(numero)
FIN
'''
#Función para sumar n números del 1 al n
# def sumaNnumeros(cantidadNumeros):
#     suma=0
#     for i in range(1,cantidadNumeros+1):# 1 2 3 4 5
#         suma+=i
#     return suma

# #Tipo void para verificar si número es par o impar
# def ParImpar(numero):
#     if numero % 2== 0:
#         print("Es par")
#     else:
#         print("Es impar")

def MostrarMensaje(user, email):
    print(f'Bienvenido, {user}. Tu correo es {user}@{email}.com')


# #Programa principal
user=input("Digita tu nombre: \n")
email=input("Compañia de correo electrónico: \n")
MostrarMensaje(user, email)
# resultado=sumaNnumeros(n)
# print("La suma de los ",n," números es: ",resultado)
# print("-----Ya regresé de la función-----")
# #LLamado al tipo void ParImpar
# ParImpar(n)
# print("Terminó el tipo void")

