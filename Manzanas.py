  
#Calcular los descuentos si 
'''
la persona compra 18 manzanas se aplica un descuento secreto de 20
si el clientye se llama igual que tu, se aplica descuento secreto de 20
si el cliente compra mas de 10v mananas se aplica el 10

los descuento no son acumulables'''
precioDeManzana = 5
cantidadDeManzana = int(input("¿Cuántas manzanas compraste? "))
nombreCliente = input("Ingresa tu nombre")
nombreCliente = "Aurora" 


descuento = (cantidadDeManzana * precioDeManzana) * 0.10
descuento_secreto = (cantidadDeManzana * precioDeManzana) * 0.20


if  cantidadDeManzana == 18 or nombreCliente == "Aurora":
    print("Tu precio con descuento secreto es:", descuento_secreto )  
elif cantidadDeManzana >10:
    print("Tu precio con  descuento es:", descuento)

if descuento > 0:
    print("El descuento fue:", descuento)   
    print("Total a pagar:", {(precioDeManzana*cantidadDeManzana)-descuento})

    
    