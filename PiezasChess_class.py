class Piezas:
    def __init__(self, tipo, nombre, color, movimiento, cantidad, captura): #posicion
        self.tipo = tipo
        self.nombre = nombre
        self.color = color
        self.movimiento = movimiento
        self.cantidad = cantidad
        self.captura = captura
        #self.posicion[letra][numero] = posicion
    
    def forma_mover(self):
        return f"{self.nombre} {self.color} se puede mover de forma {self.movimiento}, tiene un total de {self.cantidad} {self.tipo}"
    
    def capturar(self):
        return f"{self.nombre} {self.color} puede capturar piezas de forma {self.movimiento}"   

    def movement(self):
        print(f"La pieza {self.nombre} {self.color} ahora está en la posición {self.letra}{self.numero}")  
        self.letra = input("Ingrese el movimimento (Columna/Letra): ")
        self.numero = input("Ingrese el movimimento (Fila/Numero): ")
        return f"La pieza {self.nombre} {self.color} ahora está en la posición {self.letra}{self.numero}"


#main
#def Main():

#if __name__ == "__main__":
    #Main()

