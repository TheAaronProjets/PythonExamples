import pygame
import random
from tkinter import messagebox as MessageBox

"""
La biblioteca **PyGame** se emplea como el motor principal para el desarrollo del juego. 

Utilizamos el módulo **random** para seleccionar de manera aleatoria 
al jugador inicial en el juego de tic-tac-toe, asignando 'O' o 'X'. 

Para anunciar el ganador al final de la partida, 
hacemos uso de **messagebox** perteneciente a la biblioteca **tkinter**, 
la cual nos permite mostrar un mensaje emergente con el resultado.
"""

class Game:
    """
    Clase principal del juego de Tic Tac Toe.
    Utiliza Pygame para la interfaz gráfica y Tkinter para mostrar mensajes emergentes.
    """
    def __init__(self):
        """
        Inicializa el juego.
        - Crea la ventana de Pygame.
        - Inicializa el tablero.
        - Selecciona al azar el jugador que iniciará la partida.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))  # Tamaño de la ventana
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = [' '] * 9  # Tablero de juego, inicialmente vacío
        self.current_turn = random.choice(['X', 'O'])  # Turno actual, seleccionado al azar
        self.tablero = [[' ' for _ in range(3)] for _ in range(3)]  # Tablero 3x3
        # Coordenadas para el centro de cada celda del tablero
        self.cell_centers = [
            (250, 170), (640, 170), (1030, 170),
            (250, 360), (640, 360), (1030, 360),
            (250, 550), (640, 550), (1030, 550)
        ]
        # Combinaciones ganadoras posibles
        self.combinaciones_ganadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontales
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticales
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]

    def run(self):
        """
        Inicia el bucle principal del juego.
        """
        while self.running:
            self.dt = self.clock.tick(60) / 1000  # Control de FPS
            self.handle_events()
            self.draw()

    def handle_events(self):
        """
        Maneja los eventos del juego.
        - Detecta eventos de salida del juego.
        - Detecta clics del mouse y los maneja.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event.pos)
                self.verificar_ganador()  # Verificar si hay un ganador después de cada turno
    
    def handle_mouse_click(self, pos):
        """
        Maneja el clic del mouse en el tablero.
        Actualiza el tablero con la marca del jugador actual.
        """
        for i, (x, y) in enumerate(self.cell_centers):
            # Verificar si el clic fue dentro de una celda del tablero
            if pygame.Rect(x - 50, y - 50, 100, 100).collidepoint(pos):
                fila, columna = i // 3, i % 3
                if self.tablero[fila][columna] == ' ':
                    # Actualizar el tablero con la marca del jugador actual
                    self.tablero[fila][columna] = self.current_turn
                    # Cambiar el turno al otro jugador
                    self.current_turn = 'O' if self.current_turn == 'X' else 'X'
                    break

    def draw(self):
        """
        Dibuja el tablero, las marcas (X y O) y el fondo de la ventana.
        """
        self.screen.fill("black")
        self.draw_lines()
        self.draw_marks()
        pygame.display.flip()

    def draw_lines(self):
        """
        Dibuja las líneas del tablero de Tic Tac Toe.
        """
        pygame.draw.line(self.screen, (255, 255, 255), (100, 480), (1180, 480), 5)  # Línea horizontal inferior
        pygame.draw.line(self.screen, (255, 255, 255), (100, 240), (1180, 240), 5)  # Línea horizontal superior
        pygame.draw.line(self.screen, (255, 255, 255), (400, 100), (400, 620), 5)  # Línea vertical izquierda
        pygame.draw.line(self.screen, (255, 255, 255), (800, 100), (800, 620), 5)  # Línea vertical derecha

    def draw_marks(self):
        """
        Dibuja las marcas (X y O) en el tablero.
        """
        for fila in range(3):
            for columna in range(3):
                mark = self.tablero[fila][columna]
                x, y = self.cell_centers[fila * 3 + columna]
                if mark == 'X':
                    self.draw_x(x, y)
                elif mark == 'O':
                    self.draw_o(x, y)

    def draw_x(self, x, y):
        """
        Dibuja una X en la posición dada.
        """
        pygame.draw.line(self.screen, (255, 255, 255), (x - 40, y - 40), (x + 40, y + 40), 5)
        pygame.draw.line(self.screen, (255, 255, 255), (x + 40, y - 40), (x - 40, y + 40), 5)

    def draw_o(self, x, y):
        """
        Dibuja un O en la posición dada.
        """
        pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 40, 5)

    def verificar_ganador(self):
        """
        Verifica si hay un ganador en el juego.
        - Comprueba si alguna combinación de marcas es ganadora.
        - Muestra un mensaje emergente con el resultado.
        """
        for combinacion in self.combinaciones_ganadoras:
            # Verificar si hay una combinación ganadora en el tablero
            if (self.tablero[combinacion[0] // 3][combinacion[0] % 3] ==
                self.tablero[combinacion[1] // 3][combinacion[1] % 3] ==
                self.tablero[combinacion[2] // 3][combinacion[2] % 3] != ' '):
                ganador = self.tablero[combinacion[0] // 3][combinacion[0] % 3]
                MessageBox.showinfo("Ganador", f"El ganador es {ganador}")
                self.running = False
                return

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
