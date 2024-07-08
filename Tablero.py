def letra_a_columna(letra):     # Convierte letra a número de columna (0 a 7)
    return ord(letra.lower()) - ord('a')

class Tablero:
    def __init__(self):
        self.tablero = [
            ["♛","♞","♝","♛","♚","♝","♞","♛"],
            ["♟","♟","♟","♟","♟","♟","♟","♟"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["♙","♙","♙","♙","♙","♙","♙","♙"],
            ["♕","♘","♗","♕","♔","♗","♘","♕"]
        ]
        
    def mostrar_tablero(self):
        for linea in self.tablero:
            print(linea)
            
    def colocar_pieza(self, fila, columna, pieza):
        if self.tablero[fila][columna] == " ":
            self.tablero[fila][columna] = pieza
            print(f"Peón {pieza.color} colocado en fila {fila}, columna {columna}.")
        else:
            print(f"Ya hay una pieza en fila {fila}, columna {columna}.")