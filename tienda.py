print("************************")
print("**     BIENVENIDO A   **")
print("** LA TIENDA DE MASCOTAS **")
print("************************")

inventario = {
    "perro": 10,
    "gato": 8,
    "pajaros": 25,
    "iguana": 2
}

animales_totales = 0
for val in inventario.values():
    animales_totales += val

print("Por favor ingresa tu nombre")
nombre = input()

print("Por favor escribe tu apellido")
apellido = input()

# Concatenación
nombre_completo = nombre + " " + apellido

print("Gracias por visitarnos,", nombre_completo)

def mostrar_menu():
    print("")
    print("Selecciona la opción que deseas:")
    print("1: Conocer cuántos animales tiene la tienda")
    print("2: Comprar un animal")
    print("3: Salir del programa")

def mostrar_inventario():
    print("**** INVENTARIO ****")
    for llave, valor in inventario.items():
        print(f"    {llave}: {valor}")
    print("En total tenemos", animales_totales, "animales")

def comprar_animal():
    carrito = []

    while True:
       print("¿Qué animal deseas comprar? solo puedes elejir 1 de cada especie")
       print("Escrive F para terminar la lista, o V para ver tu carrito")
       animal = input()

       if animal == "F": break

       if animal == "V":
           print(f"Tu carrito de compras contiene{carrito}") 
           continue
       
       if animal not in inventario:
            print(f"Lo sentimos, no contamos con el animal {animal}")
       elif inventario[animal] == 0:
            print(f"Lo sentimos, no tenemos en existencia el animal {animal}")
       elif animal not in carrito:
            carrito.append(animal)
       else:
           print("Ese animal ya se encuentra en tu carrito")
       #print("Has comprado un", animal)
       carrito.append(animal)
       #print("Has comprado un", animal)

    print("El contedino de tu carrito es")
    for animal in carrito:
        print(" ",animal)   
        inventario[animal] -=1

while True:
    mostrar_menu()

    respuesta = int(input())

    if respuesta == 1:
        mostrar_inventario()

    elif respuesta == 2:
        comprar_animal()

    elif respuesta == 3:
        print("Saliendo del programa")
        break                   
