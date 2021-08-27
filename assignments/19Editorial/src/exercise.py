import math
palabras = int(input("Dame el número de palabras: "))
paginas = math.ceil(palabras/475)

costo = paginas * 60
descuento = costo * 0.10
total = costo - descuento

print("el costo de la publicación es:",total)