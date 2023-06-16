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
nombre = input("Ingresa tu nombre:")
primer_apellido = input("Ingresa tu apellido paterno:")
segundo_apellido = input("Ingresa tu apellido materno:")

ape_paterno = primer_apellido

print("\tAqui se va juntando la curp:  ")
print(ape_paterno[:2])