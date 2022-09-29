#DICCIONARIOS Tipos de datos compuestos--->Diccionario, Listas
#Propiedad -> clave:valor
#Representa múltipes propiedades es una sola variable
#Ejemplo---> Programación:Definición
#En los diccionarios podemos: agregar, remover, etc Las mismas que #hicimos en las listas
#Pueden cambiar su contenido en tiempo de ejecución. Mutable

#CREACIÓN DE UN DICCIONARIO

# 1. Creación de diccionario

#Esquema 1: Literal---> {}
diccionario_1 ={'propiedad1':1,'propiedad2':2,'propiedad3':[1,2,3,]}

#Esquema 2: con la clase dict
diccionario_2=dict()
diccionario_2['propiedad1']=1
diccionario_2['propiedad2']=2
diccionario_2['propiedad3']=[1,2,3]
print()
print("Diccionario 1")
print(diccionario_1)
print(diccionario_2)

print()

#Creación de un diccionario para almacenar datos de un PC

computador={
    'id':1001,
    'marca':'MSI',
    'ram':128,
    'cpu':'Intel Core i7',
    'almacenamiento':8
    }

print(computador) #Imprimimos la representación en cadena de caracteres

print("Cantidad de propiedades")
print(f'La variables diccionario `computador`tiene {len(computador)} propiedades')

print('El tipo de dato de la variable `computador` es: %s' % type(computador).__name__)

#2. Acceso a las propiedades y valores de un diccionario
print('Acceso a las propiedades y valores de un diccionario')
print(f"ID: {computador['id']}")
print(f"Marca: {computador['marca']}")
print(f"RAM: {computador['ram']}")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']}")

print(computador.get('ram'))

print()
#3. Modificación del contenido de un diccionario - mutar

computador['marca']='Movistar'
computador['id']=2001

#La modificación abarca la adición de nuevas propiedades - mutar
computador['gpu']='NVIDIA Geforce'

print(f"ID: {computador['id']}")
print(f"Marca: {computador['marca']}")
print(f"RAM: {computador['ram']}")
print(f"CPU: {computador['cpu']}")
print(f"Almacenamiento: {computador['almacenamiento']}")
print(f"GPU: {computador['gpu']}")

print()
#3. Iteraración de  un diccionario 
print("3. Iteraración de  un diccionario ")
#3.1 Iteración por las llaves de un diccionario - método keys()
print("3.1 Iteración por las llaves de un diccionario")

for k in computador.keys():
    #print(k,computador[k]) #la llave y su respectivo valor
    print(f'{k.upper()}: {computador[k]}')

print()

#3.2 Iteración por los valores de un diccionario - método values()
print("3.2 Iteración por los valores de un diccionario")
for v in computador.values():
    print(v)

print()

#3.3 Iteración por las llaves y los valores de un diccionario - método items()
print("3.3 Iteración por las llaves y los valores de un diccionario")
for k, v in computador.items():
    #print(k,v)
    print(f'{k.upper()}: {v}')


#Función sum

productos={'mouse':50000,'teclado':123000,'cpu':1345000,'monitor':450000}

total=productos.values()
print(f'Valores: {total}')

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