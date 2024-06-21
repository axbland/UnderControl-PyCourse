class Piezas:
    def __init__(self, tipo, nombre, color, movimiento, cantidad, captura):
        self.tipo = tipo
        self.nombre = nombre
        self.color = color
        self.movimiento = movimiento
        self.cantidad = cantidad
        self.captura = captura
    
    def mover(self):
        return f"{self.nombre} {self.color} se puede mover de forma {self.movimiento}, tiene un total de {self.cantidad} {self.tipo}"
    
    def capturar(self):
        return f"{self.nombre} {self.color} puede capturar piezas de forma {self.movimiento}"   
        
#main
#def Main():

#if __name__ == "__main__":
    #Main()
