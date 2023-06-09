  
#Calcular los descuentos si 
'''
la persona compra 18 manzanas se aplica un descuento secreto de 20
si el clientye se llama igual que tu, se aplica descuento secreto de 20
si el cliente compra mas de 10v mananas se aplica el 10

los descuento no son acumulables'''


cantidadDeManzana = int(input("¿Cuántas manzanas compraste? "))
print("Si quieres comprar mas manzanas presiona 1 de lo contrario 0")

while (cantidadDeManzana != 0  ):
    
  contador = 0
  contador = contador + 1
  
  nombreCliente = input("Ingresa tu nombre")
  nombreCliente = "Aurora" 
  precioDeManzana = 5
  descuento = (cantidadDeManzana * precioDeManzana) * 0.10
  descuento_secreto = (cantidadDeManzana * precioDeManzana) * 0.20
  if  cantidadDeManzana == 18 or nombreCliente == "Aurora":
    print("Tu precio con descuento secreto es:", descuento_secreto )  
  elif cantidadDeManzana >10:
    print("Tu precio con  descuento es:", descuento)

  if descuento > 0:
    print("El descuento fue:", descuento)   
    print("Total a pagar:", {(precioDeManzana*cantidadDeManzana)-descuento})
  
  print("Si quieres comprar mas manzanas presiona 1 de lo contrario 0")
  

  
    
    



    
    


