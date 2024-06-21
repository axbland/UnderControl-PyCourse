from PiezasChess_class import Piezas

class Alfil(Piezas):
    def __init__(self, tipo, nombre, color, movimiento, cantidad, captura):
        super().__init__(tipo, nombre, color, movimiento, cantidad, captura)