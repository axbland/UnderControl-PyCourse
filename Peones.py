from PiezasChess_class import Piezas

class Peon(Piezas):
    def __init__(self, tipo, nombre, color, movimiento, cantidad, captura):
        super().__init__(tipo, nombre, color, movimiento, cantidad, captura)
        
    def promo(self):
        return f"El {self.nombre} {self.color} se puede promocionar a un alfil, torre o dama"  