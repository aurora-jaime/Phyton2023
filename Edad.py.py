# NOMBRE / APELLIDO PATERNO / APELLIDO MATERNO / FECHA DE NACIMIENTO

nombre = input("Ingresa nombre:")
ape_paterno = input("Ingresa el apellido paterno:")
ape_materno = input("Ingresa el apellido materno:")
fecha_naci = input("Ingresa la fecha de nacimiento:")

nombre_completo = ape_paterno + ape_materno

cadena = nombre_completo
print(cadena[2])  # Se corrige el índice a [2] para obtener el tercer carácter (índice 2)