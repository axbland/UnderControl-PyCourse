class Piezas:
    def __init__(self, nombre, color, movimiento, cantidad, captura):
        self.nombre = nombre
        self.color = color
        self.movimiento = movimiento
        self.cantidad = cantidad
        self.captura = captura
    
    def mover(self):
        return f"{self.nombre} {self.color} se puede mover de forma {self.movimiento}"
    
    def capturar(self):
        return f"{self.nombre} {self.color} puede capturar piezas de forma {self.movimiento}"

class Peon(Piezas):
    def __init__(self, nombre, color, movimiento, cantidad, captura):
        super.__init__(nombre, color, movimiento, cantidad, captura)
    
    def promo(self):
        return f"El {self.nombre} {self.color} se puede promocionar a un alfil, torre o dama"
        
    
class Torre(Piezas):
    def __init__(self, nombre, color, movimiento, cantidad, captura):
        super.__init__(nombre, color, movimiento, cantidad, captura)
    
class Alfil(Piezas):
    def __init__(self, nombre, color, movimiento, cantidad, captura):
        super.__init__(nombre, color, movimiento, cantidad, captura)
    
class Rey(Piezas):
    def __init__(self, nombre, color, movimiento, cantidad, captura):
        super.__init__(nombre, color, movimiento, cantidad, captura)
    
class Dama(Piezas):
    def __init__(self, nombre, color, movimiento, cantidad, captura):
        super.__init__(nombre, color, movimiento, cantidad, captura)
    
class Caballo(Piezas):
    def __init__(self, nombre, color, movimiento, cantidad, captura):
        super.__init__(nombre, color, movimiento, cantidad, captura)