precioDeManzana = 5
cantidadDeManzana = int(input("¿Cuántas manzanas compraste? "))

# input recibe valores de tipo string
# el int antes del input es para que solo nos pregunte números enteros

descuento = (cantidadDeManzana * precioDeManzana) * 0.10

if cantidadDeManzana >= 10:
    print("Va a pagar con descuento:", descuento)

if descuento > 0:
    print("El descuento fue:", descuento)

