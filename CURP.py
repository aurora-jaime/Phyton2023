#NOMBRE / APELLIDO PATERNO / APELLIDO MATERNO / FECHA DE NACIMIENTO 

nombre = print(input("Ingresa nombre:"))
ape_paterno = print(input("Ingresa el apellido paterno:"))
ape_materno = print(input("Ingresa el apellido materno:"))
fecha_naci = print(input("Ingresa la fecha de nacimiento:"))

nombre_completo = ape_materno + ape_paterno
string = nombre_completo
words = string.split(' ') 
character = ''

for word in words:
   character += word[0]

print(character)
