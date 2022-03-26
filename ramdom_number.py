# Con este tienes vidas ilimitadas

# import random

# def run():
#     numero_aleatorio = random.randint(1, 100)
#     numero_elegido = int(input("Elige un número del 1 al 100: "))
#     while numero_elegido != numero_aleatorio:
#         if numero_elegido < numero_aleatorio:
#             print("busca un número más grande")
#         else:
#             print("busca un número más pequeño")
#         numero_elegido = int(input("Elige otro número: "))
#     print("Ganaste")

# if __name__  == "__main__":
#     run()

# Con este tienes 5 vidas

import random

def run():
    numerorandom = random.randint(1, 100)
    numeroelegido = int(input("Introduce un numero: "))
    vidas = 5
    while numerorandom != numeroelegido :
        if numerorandom < numeroelegido : 
            print("Elige un numero mas pequeño.")
            vidas -= 1
        elif numerorandom > numeroelegido : 
            print("Elige un numero mas grande.")
            vidas -= 1
        if vidas == 0 :
            print("GAME OVER")
            break
        print("Tienes", vidas, "vidas")
        numeroelegido = int(input("Introduce numero: "))
    if numerorandom == numeroelegido : 
        print("FELICIDADES GANASTE")


if __name__ == "__main__" : 
    run()