"""
SABER SI UN NUMERO ES O NO ES PRIMO
"""

# Solicita al usuario que ingrese un número entero
num = abs(int(input("Ingrese un número entero: ")))

# Un número menor que 2 no es primo
if num < 2:
    print("El número no es primo")
else:
    # Asumimos que el número es primo hasta que se demuestre lo contrario
    es_primo = True

    # Verificamos si el número tiene algún divisor distinto de 1 y de sí mismo
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break

    # Imprimimos el resultado
    if es_primo:
        print("Es un número primo")
    elif es_primo == False:
        print("El número no es primo")
    else:
        print("Es un producto norteño")
        print("Como terminaste aca flaco?")
    