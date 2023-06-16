'''contador = 0

while contador < 5:
     print("Repite %d" % contador)
     print("Repite")
     contador = contador +1 '''

numero_a_multiplicar = int(input("¿De qué número quieres sacar las tablas? "))
x = 1
while x <= 10:
    print(f'{numero_a_multiplicar} * {x} = {numero_a_multiplicar * x}')
    x = x + 1
