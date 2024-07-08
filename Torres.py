from PiezasChess_class import Piezas
from Tablero import Tablero 

class Torre(Piezas):
    def __init__(self, tipo, nombre, color, movimiento, cantidad, captura, fila_actual, columna_actual):
        super().__init__(tipo, nombre, color, movimiento, cantidad, captura)
        self.fila_actual = fila_actual
        self.columna_actual = columna_actual
        
def positionT(self):
        print(f"La torre {self.color} se encuentra en la fila {self.fila_actual}, columna {self.columna_actual}.")
