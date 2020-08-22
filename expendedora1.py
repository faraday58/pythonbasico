numProducto=input(" Introduzca le número del producto deseado \n  1A)papas \n 2B)Refresco \n 3C)Chocolate \n ")
print("Usted seleccionó el producto: ",numProducto)
if numProducto == "1A":
    precio=10
if numProducto == "2B":
    precio=12
if numProducto == "3C":
    precio=15
print("El precio del producto es: $",precio)

efectivo=float(input("Introduzca efectivo "))

cambio=efectivo-precio

print(" Entregando producto ")
cambio= "$" + str(cambio)
print("El cambio es: ",cambio)
