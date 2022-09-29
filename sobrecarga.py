def sumarNumeros(n1,n2):
    suma=0
    suma=n1+n2
    return suma

def sumarNumeros(n1,n2,n3):
    suma=n1+n2+n3
    return suma

numero1=100
numero2=345
numero3=200

suma=sumarNumeros(numero1,numero2,numero3)
print("La suma de los tres números\n")
print(suma)

print("La suma de los dos números\n")
suma=sumarNumeros(numero1,numero2,0)
print(suma)

    