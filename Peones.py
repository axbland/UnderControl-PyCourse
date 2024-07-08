from PiezasChess_class import Piezas
from Tablero import Tablero 

class Peon(Piezas):
    def __init__(self, tipo, nombre, color, movimiento, cantidad, captura, fila_actual, columna_actual):
        super().__init__(tipo, nombre, color, movimiento, cantidad, captura)
        self.fila_actual = fila_actual
        self.columna_actual = columna_actual
        #self.primer_mov = True  
        
    def promo(self):
        return f"El {self.nombre} {self.color} se puede promocionar a un alfil, torre o dama"  
    
    #def movimiento(self, fila_nueva, columna_nueva):
        if fila_nueva == self.fila_actual + 1 and columna_nueva == self.columna_actual:
            print(f"El peón {self.color} se ha movido a la fila {fila_nueva}, columna {columna_nueva}.")
            self.fila_actual = fila_nueva
            self.columna_actual = columna_nueva
            return True
        else:
            print(f"Movimiento inválido para el peón {self.color}.")
            return False
        
    def positionP(self):
        print(f"El peón {self.color} se encuentra en la fila {self.fila_actual}, columna {self.columna_actual}.")
