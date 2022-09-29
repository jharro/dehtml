"""
Actividad Diccionarios
Deben crear un programa en python donde se va a declarar un diccionario para guardar los nombres y los precios de varias frutas.
Cada propiedad se compone del nombre de la fruta y el precio. Inicialmente el diccionario se debe crear con 5 frutas.
El programa debe permitir efectuar un CRUD y otras actividades sobre el diccionario, así:

1. Consultar: Se pedirá al usuario que ingrese el nombre de la fruta que se quiere consultar.
Al encontrarla debe mostrar su nombre y su precio. En caso contrario el mensaje "Esa fruta NO existe en la tienda".

2. Agregar: Se pedirá al usuario que ingrese el nombre de la fruta que se quiere agregar, pero si ésta ya está en el diccionario,
se mostrará el mensaje "Esa fruta ya está en la tienda". Al comprobarse que la fruta no existe,
se debe pedir su correspondiente precio y agregar la nueva fruta con su correspondiente nombre y precio (clave:valor)
y mostrar el mensaje "Fruta agregada exitosamente".

3. Modificar: Se pedirá al usuario que ingrese el nombre de la fruta a la cual se quiere modificar el precio,
pero si ésta no está en el diccionario, se mostrará el mensaje "Esta fruta no está en la tienda".
Al comprobarse que la fruta está en el diccionario, se pedirá al usuario que ingrese el nuevo precio,
el cual será actualizado en el diccionario, y se mostrará el mensaje "El precio de la fruta se ha actualizado exitosamente".

4. Borrar: Se pedirá al usuario que ingrese el nombre de la fruta que se desea eliminar.
Al comprobarse que la fruta no está en el diccionario, se debe mostrar el mensaje "La fruta no existe en la tienda".
En el caso que existiera en el diccionario, se deberá eliminar la fruta (clave:valor)
y mostrar el mensaje "La fruta ha sido eliminada exitosamente".

5. Listar frutas:  Al seleccionar esta opción, se debe mostrar el listado de las frutas con sus correspondiente nombre y precios. listo pa

6. Inventario: Al seleccionar esta opción, se debe mostrar la cantidad de frutas que hay en la tienda, el valor del inventario,
que corresponde a la suma de los precios de todas las frutas y el precio promedio de las frutas.

7. Terminar:  Al seleccionar esta opción, se debe terminar la ejecución del programa



"""

from __future__ import barry_as_FLUFL
from ast import While
from optparse import Values

def consultar():
    ingreso = str(input("ingrese que fruta desea consultar: "))
    for i in frutas:
        if ingreso == i:
            print(f"el precio de {i} es = {frutas[i]}")
            break

        
    else:
        print("Esa fruta NO existe en la tienda")

def agregar():
    d = str(input("ingrese el nombre de la fruta que quiere agregar: "))
    if d in frutas:
        print("esta fruta ya esta en la tienda")
        
    else:
        valor = int(input("ingrese el valor: "))
        frutas[d]= valor
        print("su fruta se agregado con exito")

def modificar():
    d = str(input("ingrese el nombre de la fruta a la cual se quiere modificar el precio: "))
    if d in frutas:
        valor = int(input("ingrese el precio nuevo que quiere ingresar: "))
        frutas[d]=valor
        print("El precio de la fruta se ha actualizado exitosamente")
    else:
        print("esta fruta no esta en la tienda")
        
def borrar():
    d = str(input("ingrese el nombre de la fruta que se desea eliminar: "))
    if d in frutas:
        del frutas[d]
        print("La fruta ha sido eliminada correctamente")
    else:
        print("La fruta no existe en la tienda")
        
def listar():
    for k in frutas.keys():
        print(f'---------->>  {k} = {frutas[k]}')

def inventario():
    cantidad_frutas=len(frutas)
    lasuma=sum(frutas.values())
    promedio = lasuma / cantidad_frutas
    print()
    print(f"La cantidad de inventario es de: {cantidad_frutas}")
    print(f"El valor del inventario es de: : {lasuma}")
    print(f"El promedio del inventario es de: {promedio}")
    print()
    
def cliente():
    continua = True
    sub_total=0
    while continua:
            print("---------------------------------")
            print("El siguiente listado son de las frutas disponible.")
            print("---------------------------------")
            for k in frutas.keys():
                print(f'---------->>  {k} = {frutas[k]}')
                
            d = str(input("ingrese la fruta que quiere adquirir: "))
            if d in frutas:
                valor=frutas.get(d)
                cantidad = int(input("ingrese la cantidad que desee comprar: "))
                total= valor * cantidad
                sub_total = sub_total + total
                print(f"llevas de compra {sub_total}")
            ingreso = str(input("Si desea continuar oprima: 1\nSi no deseas continuar oprima: 2\n="))
            
            if ingreso == "1":
                print(f"por el momento llevas: {total}")
                continue
            
            if ingreso == "2":
                print(f"El pago final es de: {sub_total}")
                continua = False
    return sub_total

def total_dia(e):
    print("------------------------------")
    print(f"las ventas del dia fueron = {e}")
    print("------------------------------")

frutas={
"fresa":3000,
"lulo":2500,
"manzana":2000,
"mandarina":1200,
"papaya":7000
}


mundo = 0

while True:
    d = int(input('-----------------OPCIONES---------------------\n'
    '       si deseas consultar oprima......#1\n       si deseas agregar oprima........#2\n'
    '       si deseas modificar oprima......#3\n       si deseas borrar oprima.........#4\n'
    '       si deseas listar oprima.........#5\n       si deseas inventario oprima.....#6\n'
    '       si deseas comparar oprima.......#7\n       si deseas ver las venta del dia.#8\n'
    '       si deseas terminar oprima.......#9\n'
    '----------------------------------------------\n'
    'ingrese el numero = '))
    if d == 1:
        consultar()
    elif d == 2:
        agregar()
    elif d == 3:
        modificar()
    elif d == 4:
        borrar()
    elif d == 5:
        listar()
    elif d == 6:
        inventario()
    elif d == 7:
        mundo=cliente()
    elif d == 8:
        total_dia(mundo)
    elif d == 9:
        print("ha terminado la interaccion")
        break
    else:
        print("El numero que ha ingresado no se encuentra disponible")
