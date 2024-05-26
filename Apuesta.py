import random
"""
Juego de "Apuestas" pide a 2 Jugadores un dinero inicial
Se tiran dos dados aleatorios por jugador, gana el jugador que sume 7 primero
si ninguno suma 7 gana la Casa
"""
class JuegoDadosDosJugadores:
    # Método constructor, se ejecuta al crear una instancia de la clase
    def __init__(self):
        # Solicita el dinero inicial para el Jugador 1
        self.dinero_jugador1 = int(input("Jugador 1: Cuanto dinero tienes: "))
        # Solicita el dinero inicial para el Jugador 2
        self.dinero_jugador2 = int(input("Jugador 2: Cuanto dinero tienes: "))

    # Método para lanzar los dados, retorna dos números aleatorios entre 1 y 6
    def lanzar_dados(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        return dado1, dado2

    # Método principal del juego
    def jugar(self):
        # El juego continúa mientras ambos jugadores tengan dinero
        while self.dinero_jugador1 > 0 and self.dinero_jugador2 > 0:
            # Solicita la apuesta del Jugador 1
            self.apuesta_j1 = int(input("(Jugador 1): Cuanto quieres apostar: "))
            # Solicita la apuesta del Jugador 2
            self.apuesta_j2 = int(input("(Jugador 2): Cuanto quieres apostar: "))
            
            # Verifica que las apuestas no superen el dinero disponible de cada jugador
            if self.apuesta_j1 < self.dinero_jugador1 + 1 and self.apuesta_j2 < self.dinero_jugador2 + 1:
                input("Presiona Enter para lanzar los dados:\n")
                
                # Jugador 1 lanza los dados
                dado1_j1, dado2_j1 = self.lanzar_dados()
                suma_tirada_j1 = dado1_j1 + dado2_j1
                
                # Jugador 2 lanza los dados
                dado1_j2, dado2_j2 = self.lanzar_dados()
                suma_tirada_j2 = dado1_j2 + dado2_j2
                
                # Muestra los resultados de las tiradas de ambos jugadores
                print(f"Tirada Jugador 1: {dado1_j1} + {dado2_j1} = {suma_tirada_j1}")
                print(f"Tirada Jugador 2: {dado1_j2} + {dado2_j2} = {suma_tirada_j2}")

                # Determina el resultado del juego
                if suma_tirada_j1 == 7:
                    print("¡Jugador 1 ganó!, Jugador 2 Perdio")
                    # Jugador 1 gana las apuestas de ambos jugadores
                    self.dinero_jugador1 += (self.apuesta_j2 + self.apuesta_j1)
                    self.dinero_jugador2 -= self.apuesta_j2
                elif suma_tirada_j2 == 7:
                    print("¡Jugador 2 ganó!, Jugador 1 Perdio")
                    # Jugador 2 gana las apuestas de ambos jugadores
                    self.dinero_jugador1 -= self.apuesta_j1
                    self.dinero_jugador2 += (self.apuesta_j2 + self.apuesta_j1)
                else:
                    print("Ambos perdieron su dinero :( ")
                    # Ambos jugadores pierden sus apuestas
                    self.dinero_jugador1 -= self.apuesta_j1
                    self.dinero_jugador2 -= self.apuesta_j2

                # Muestra el dinero actual de ambos jugadores
                print(f"Dinero actual Jugador 1: {self.dinero_jugador1}")
                print(f"Dinero actual Jugador 2: {self.dinero_jugador2}\n")
            else:
                # Mensaje de error si una apuesta supera el dinero disponible
                print("Uno de los jugadores aposto mas dinero del que tiene.")
        
        # Fin del juego, uno de los jugadores se ha quedado sin dinero
        print("¡Se acabó el juego! Uno de los jugadores se quedó sin dinero.")

# Punto de entrada del programa
if __name__ == "__main__":
    # Crea una instancia del juego y lo inicia
    juego = JuegoDadosDosJugadores()
    juego.jugar()
