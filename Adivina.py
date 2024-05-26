import random

"""
Adivina el número aleatorio
"""

# Genera un número aleatorio entre 0 y 50
x = random.randint(0, 50)

# Número de intentos permitidos
intos = 6

# Bucle que permite al usuario adivinar el número en hasta 6 intentos
for i in range(6):
    # Informa al usuario de los intentos restantes
    print(f"Te quedan {intos} intentos")
    intos -= 1
    
    # Solicita al usuario que ingrese un número entero
    num = int(input("Dime un número entero entre 0 y 50: "))
    
    # Estructura de control 'match' para comparar el número ingresado con el número aleatorio
    match num:
        # Caso donde la diferencia es de 10 o más
        case n if n >= x + 10 or n <= x - 10:
            print("Estás lejos del número.")
        
        # Caso donde la diferencia es entre 5 y 9
        case n if n >= x + 5 or n <= x - 5:
            print("Estás cerca del número.")
        
        # Caso donde la diferencia es entre 2 y 4
        case n if n >= x + 2 or n <= x - 2:
            print("Estás muy cerca del número.")
        
        # Caso donde el número es adivinado correctamente
        case _:
            print("¡Adivinaste el número!")
            break

# Mensaje final al término del juego
print("El juego ha terminado")
