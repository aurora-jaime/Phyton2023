'''
Como se saca la CURP
JA G A 011215 XN9
1. Primeras 2 letras del primer apellido
2. Primera letra del segundo apellido
3. Primera letra de tu nombre
4.Homoclave
 
 1          2 
 jaime     gutierrez
'''
import random #librerias 
import string

nombre = input("Ingresa tu nombre:")
primer_apellido = input("Ingresa tu apellido paterno:")
segundo_apellido = input("Ingresa tu apellido materno:")
ano = int(input("Ingresa tu año de nacimiento:"))
mes = int(input("Ingresa tu mes de nacimiento:"))
dia = int(input("Ingresa tu día de nacimiento:"))

ape_pa = primer_apellido
ape_ma = segundo_apellido 
ultimos_dos_digitos = ano % 100

def homoclave():
    letras = string.ascii_uppercase
    num = string.digits
    homo = ''.join(random.choices(letras, k=3))
    homo += ''.join(random.choices(num, k=2))

print("\tAqui se va juntando la curp:  ")
print(ape_pa[:2].upper(), ape_ma[:1].upper(), nombre[:1].upper(), ultimos_dos_digitos, mes, dia, homoclave(homoclave))





