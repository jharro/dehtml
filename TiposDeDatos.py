"""#NÚMERICOS: Enteros - Decimal
valor1=100.78

print(type(valor1))
#ALFANUMÉRICOS: Cadena - Caracter
nombre="Juan"
print(type(nombre))
simbolo='a'
print(type(simbolo))

#LÓGICO: True False
logico=True
print(type(logico))"""

mensaje="Hola"
nombre="Sara Fernández"
edad=34
salario=3500000

# Hola Sara Fernández, bienvenida. Tienes 34 años y tu salario es de 3500000
print(mensaje+" " +nombre+", bienvenida. Tienes "+str(edad)+" años y tu salario es de ",salario)

#f
print(f'{mensaje} {nombre} , bienvenida. Tienes {edad} años y tu salario es de {salario*0.10}')

#https://pythontutor.com/visualize.html

valor1=100
valor2=200

#100 * 200 = 20000

print(f'{valor1}*{valor2} = {valor1*valor2}')
