"""
Conversión de temperatura
Celsius, Farenheit, Kelvin
"""

# Solicita al usuario que ingrese una temperatura
x = float(input("Dime los grados: "))

# Solicita al usuario que indique el tipo de grados ingresados
Grado = int(input("¿Qué tipo de grados son? Escribe \n1 (Celsius), 2 (Farenheit), 3 (Kelvin): "))

# Estructura de control 'match' para convertir la temperatura según el tipo de grados ingresados
match Grado:
    # Caso para grados Celsius
    case n if n == 1:
        # Convierte Celsius a Farenheit
        CelsiFa = round((x * 9/5) + 32, 2)
        # Convierte Celsius a Kelvin
        CelsiKe = round(x + 273.15, 2)
        # Imprime los resultados de las conversiones
        print(f"Los {x} grados Celsius son equivalentes a \n {CelsiFa} grados Farenheit y {CelsiKe} grados Kelvin")
    
    # Caso para grados Farenheit
    case n if n == 2:
        # Convierte Farenheit a Celsius
        FarenCe = round((x - 32) * 5/9, 2)
        # Convierte Farenheit a Kelvin
        FarenKe = round((x - 32) * 5/9 + 273.15, 2)
        # Imprime los resultados de las conversiones
        print(f"Los {x} grados Farenheit son equivalentes a \n {FarenCe} grados Celsius y {FarenKe} grados Kelvin")
    
    # Caso para grados Kelvin
    case n if n == 3:
        # Convierte Kelvin a Celsius
        KelviCe = round(x - 273.15, 2)
        # Convierte Kelvin a Farenheit
        KelviFa = round((x - 273.15) * 9/5 + 32, 2)
        # Imprime los resultados de las conversiones
        print(f"Los {x} grados Kelvin son equivalentes a \n {KelviCe} grados Celsius y {KelviFa} grados Farenheit")
    
    # Caso por defecto, si el usuario ingresa un tipo de grado no válido
    case _:
        print("Error: Tipo de grados no válido")
