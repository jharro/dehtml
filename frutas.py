#Se necesita la extension pandas
import pandas as pd
import numpy as nm

frutas=dict(
bananos ={'nombre':'bananos','precio':3000,'cantidad': 5},
fresas ={'nombre':'fresas','precio':500,'cantidad': 50},
manzanas ={'nombre':'manzanas','precio':1500,'cantidad': 10},
maracuya ={'nombre':'maracuya','precio':2000,'cantidad': 20},
uvas ={'nombre':'uvas','precio':600,'cantidad': 42}
)
frutas2= pd.DataFrame({'precio':[3000,500,1500,2000,600],'cantidad':[5,50,10,20,42], 'nombre':['bananos','fresas','manzanas','maracuya','uvas']})

def consultar(a):
    if frutapreg in frutas2.index:  
        print(frutas2[frutas2.index==frutapreg])
    else:
        print("Esa fruta NO existe en  la tienda")
        
def insertar(b, c, d):
    if frutapreg not in frutas2.index:
        frutas2.loc[b]=[c,d]
        print("Fruta agregada exitosamente")
    else: 
        print("Esa fruta ya está en la tienda")

def modificar(a):
    if frutapreg in frutas2.index:
        modifprecio=(int(input("que nuevo precio le quieres poner?: ")))
        frutas2.loc[a, ['precio']] = [modifprecio]
        print("El precio de la fruta se ha actualizado exitosamente")
    else:
        print("Esta fruta no está en la tienda")

def eliminarfruta(a):
    if a in frutas2.index:
        frutas2.drop([a], inplace=True)
        print("La fruta ha sido eliminada exitosamente")

    else:
        print("La fruta no existe en la tienda")

def multiplicar():
        precios= frutas2['precio']
        cantidad= frutas2['cantidad']
        preciounit=precios*cantidad
        valortotal=sum(preciounit)
        print("el valor total del inventario es: ", valortotal)

def cantidadfrutas():
        cantidad= frutas2['cantidad']
        totalfrutas= sum(cantidad)
        print("la cantidad total de frutas es: ",totalfrutas)

def modificarcantidad(a):
    if frutapreg in frutas2.index:
        cantidadactual=frutas2.loc[a, ['cantidad']]
        frutas2.loc[a, ['cantidad']] = [cantidadactual-cuantasllevar]
        

frutas2.set_index('nombre', inplace=True)
hacer= (int(0)) 
ventasdia= 0      
while hacer < 9 :
    print()
    print()
    hacer=int(input(f'1.Consultar\n2.Agregar\n3.Modificar\n4.Borrar\n5.Listar\n6.Inventario\n7.vender\n8.ventas del dia\n9.terminar\nque opcion vas a escoger?\n' ))

    if hacer == 1:
        frutapreg=(str(input("cual fruta estas buscando?: ")))
        consultar(frutapreg)
    elif hacer == 2:
        frutapreg=(input("cual fruta vas a insertar?: "))
        if frutapreg in frutas2.index:
            print("Esa fruta ya está en la tienda")
        else:
            precioinsert=(int(input('cual es el precio de la fruta?: ')))
            cantidadinsert=(int(input('cuanta va a agregar?: ')))
            insertar(frutapreg, precioinsert,cantidadinsert)
    elif hacer == 3:
        frutapreg=(str(input("cual fruta estas modificando?: ")))
        modificar(frutapreg)
    elif hacer == 4:
        frutapreg=(str(input("cual fruta estas eliminando?: ")))
        eliminarfruta(frutapreg)
    elif hacer == 5:
        print(frutas2)
    elif hacer == 6:
        cantidad= frutas2['cantidad']
        totalfrutas= sum(cantidad)
        print("la cantidad total de frutas es: ",totalfrutas)
        precios= frutas2['precio']
        preciounit=precios*cantidad
        valortotal=sum(preciounit)
        print("el valor total del inventario es: ", valortotal,'$')
        promfrutas=valortotal/totalfrutas
        print("El precio medio de las frutas es: ",promfrutas,'$')
    elif hacer == 7:
        venta=0
        valorcompra= 0
        seguircomprando='si'
        while seguircomprando=='si':
            frutapreg=(str(input("cual fruta estas buscando?: ")))
            if frutapreg in frutas2.index:
                cuantasllevar=(int(input("cuantas frutas va a llevar?: ")))
                precio=frutas2.loc[frutas2.index==frutapreg, 'precio'].values[0]
                valorcompra+=precio*cuantasllevar
                modificarcantidad(frutapreg)
                ventasdia+= valorcompra
            print("su compra actual es de: ",valorcompra,'$')
            seguircomprando=(str(input("para seguir comprando escribar si: ")))
    elif hacer == 8:
        print ("las ventas del dia son de: ",ventasdia,'$')
    else: hacer=9