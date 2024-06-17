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
        super().__init__(nombre, color, movimiento, cantidad, captura)
    
    def promo(self):
        return f"El {self.nombre} {self.color} se puede promocionar a un alfil, torre o dama"     
        
#main
def Main():
    reyB = Piezas("Rey", "Blanco", "Lineal y Diagonal", 1, "Lineal y Diagonal")
    reyN = Piezas("Rey", "Negro", "Lineal y Diagonal", 1, "Lineal y Diagonal")
    print(reyN.mover())
    print(reyB.capturar())
    
    alfilB = Piezas("Alfil", "Blanco", "Diagonal", 2, "Diagonal")
    alfilN = Piezas("Alfil", "Negro", "Diagonal", 2, "Diagonal")
    
    torreB = Piezas("Torre", "Blanco", "Lineal", 2, "Lineal")
    torreN = Piezas("Torre", "Negro", "Lineal", 2, "Lineal")
    
    peonB = Peon("Peon", "Blanco", "Lineal", 8, "Lineal y Al Paso")
    peonN = Peon("Peon", "Negro", "Lineal", 8, "Lineal y Al Paso")
    print(peonN.promo())
        
    damaB = Piezas("Dama", "Blanco", "Lineal y Diagonal", 1, "Lineal y Diagonal")
    damaN = Piezas("Dama", "Negro", "Lineal y Diagonal", 1, "Lineal y Diagonal")
    
    caballoB = Piezas("Caballo", "Blanco", "L", 1, "L")
    caballoN = Piezas("Caballo", "Negro", "L", 1, "L")
    
if __name__ == "__main__":
    Main()
