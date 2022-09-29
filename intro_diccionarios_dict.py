#DICCIONARIOS Tipos de datos compuestos--->Diccionario, Listas
#Propiedad -> clave:valor
#Representa múltipes propiedades es una sola variable
#Ejemplo---> Programación:Definición
#En los diccionarios podemos: agregar, remover, etc Las mismas que #hicimos en las listas
#Pueden cambiar su contenido en tiempo de ejecución. Mutable

#CREACIÓN DE UN DICCIONARIO

# 1. Creación de diccionario

#Esquema 1: Literal---> {}

diccionario_01={
    'clave1':1,
    'clave2':2,
    'clave3':[1,2,3]
    }

print(diccionario_01)

#Esquema 2: con la clase dict
diccionario_2=dict()

diccionario_2['clave1']=1
diccionario_2['clave2']=2
diccionario_2['clave3']=[1,2,3]
print(diccionario_2)



print()

#Creación de un diccionario para almacenar datos de un PC
computador={
            'procesador':'Intel Core i9',
            'ram':64,
            'GPU':'Nvidia 3090Ti'
            }

 #Imprimimos la representación en cadena de caracteres
print(computador)
print(f'Este diccionario tiene  {len(computador)} elementos')

#2. Acceso a las propiedades y valores de un diccionario
print("PROCESADOR: ",computador['procesador']) # PROCESADOR: Intel Core i9
print(computador['ram'])
print(computador['GPU'])


print()
#3. Modificación del contenido de un diccionario - mutar
computador['procesador']='AMD'
print("Diccionario mutado en la clave procesador")
print(computador)


#La modificación abarca la adición de nuevas propiedades - mutar
computador['almacenamiento']=500
print(f'Este diccionario tiene  {len(computador)} elementos')
print(computador)
#CRUD --> Create - 
#INSERT-SELECT-UPDATE-DELETE

print()
#3. Iteraración de  un diccionario 
print("3. Iteraración de  un diccionario ")
for i in computador:
    print(computador[i])
    
#3.1 Iteración por las llaves de un diccionario - método keys()
print("3.1 Iteración por las llaves de un diccionario")
for i in computador.keys():
    print([i])



#3.2 Iteración por los valores de un diccionario - método values()
print("3.2 Iteración por los valores de un diccionario")
for i in computador.values():
    print([i])

print()

#3.3 Iteración por las llaves y los valores de un diccionario - método items()
print("3.3 Iteración por las llaves y los valores de un diccionario")
for i in computador.items():
    print([i])


#Función sum

productos={'mouse':50000,'teclado':123000,'cpu':1345000,'monitor':450000}

total=productos.values()
print("\nImpresión de los valores de los productos")
print(f'Valores: {total}') 
print(f'La suma con SUM es--> {sum(total)}')

print(f'La suma de los productos es {sum(productos.values())}')

print(list(productos))

valores=productos.values()
suma=0
for v in valores:
    suma+=v
print()

print(f'La suma de los valores es {suma}')

#3.4 Métodos y operadores para variables de tipo diccionario
#3.4.1 list(): para convertir las llaves de un diccionario en una lista

llaves=list(computador)
print(llaves)

#3.4.2 in: consulta si una llave se encuentra en un diccionario
print('board' in computador)
print('ram' in computador)

agenda_clientes={
    'cedula':102030,
    'nombre':'Sandra',
    'tele':3112323,
    'email':'micorreo@gmail.com'
    }

#1. Consultar - cédula
#2. Agregar
#3. Modificar
#4. Eliminar
#5. Salir