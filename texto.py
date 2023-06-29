datos=open('texto ejemplo.txt', 'r') #abrir y leer

while True:
    opci=int(input("\nMENÚ\n1. Contador de palabras\n2. Salir\n"))
    if opci==1:#Leer un archivo de texto y contar las palabras que tiene el texto
        cantidad=0
        for linea in datos.readlines():
            palabras=len(linea.split(" "))
            cantidad+=palabras
        print(f"El texto contiene {cantidad} palabras")
    if opci==2:
        print("Se cerrará el programa...")
        break

datos.close()