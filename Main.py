from Peones import Peon
from Torres import Torre
from Alfiles import Alfil
from Caballos import Caballo
from Dama import Dama
from Rey import Rey
from Tablero import Tablero , letra_a_columna

screen = Tablero()
screen.mostrar_tablero()

#print("** Peones **\n")    
peonB = Peon("peones blancos", "Peon", "Blanco", "Lineal", 8, "Lineal y Al Paso", 1, letra_a_columna("b")) #letra_a_columna("b") 4
peonN = Peon("peones negros", "Peon", "Negro", "Lineal", 8, "Lineal y Al Paso", 6, letra_a_columna("d")) #letra_a_columna("d") 6

#screen.colocar_pieza(peonB.fila_actual, peonB.columna_actual, peonB)
#screen.colocar_pieza(peonN.fila_actual, peonN.columna_actual, peonN)

while True:                                 # Bucle infinito que se ejecuta hasta que se encuentre una instrucción break
    
    peonN.positionP() 
    posicion = input("Ingrese la posición para el movimiento (por ejemplo, 'd7'): ")
            
    if len(posicion) != 2:              # Verifica si la longitud de la entrada del usuario es distinto a 2 caracteres
        print("La posición debe tener exactamente dos caracteres.")
        continue
            
    columna_nueva = ord(posicion[0].lower()) - ord('a')        #Convierte a letra la posición ingresada por el usuario
    fila_nueva = int(posicion[1]) - 1                   #Convierte el 2do caracter de la posición ingresada (fila) de str a int para restarle 1 y obtener el índice correcto
            
    if not (0 <= fila_nueva <= 7 and 0 <= columna_nueva <= 7):          #Verifica si la fila y la columna están dentro del rango válido del tablero
        print("Posición fuera de rango del tablero")
        continue
    
    if len(posicion) == 2:
        peonN.columna_actual = columna_nueva
        peonN.fila_actual = fila_nueva
            
    screen.colocar_pieza(peonN.fila_actual, peonN.columna_actual, peonN)
    #screen.mostrar_tablero()
    break
 
#print("** Torres **\n")    
torreB = Torre("torres blancas", "Torre", "Blanco", "Lineal", 2, "Lineal", 0, letra_a_columna("a"))
torreN = Torre("torres negros", "Torre", "Negro", "Lineal", 2, "Lineal", 7, letra_a_columna("a")) 
 
while True:                                
    
    torreB.positionT() 
    posicion = input("Ingrese la posición para el movimiento (por ejemplo, 'd7'): ")
            
    if len(posicion) != 2:              
        print("La posición debe tener exactamente dos caracteres.")
        continue
            
    columna_nueva = ord(posicion[0].lower()) - ord('a')       
    fila_nueva = int(posicion[1]) - 1                  
            
    if not (0 <= fila_nueva <= 7 and 0 <= columna_nueva <= 7):      
        print("Posición fuera de rango del tablero")
        continue
    
    if len(posicion) == 2:
        torreB.columna_actual = columna_nueva
        torreB.fila_actual = fila_nueva
            
    screen.colocar_pieza(torreB.fila_actual, torreB.columna_actual, torreB)
    #screen.mostrar_tablero()
    break

 
####################################     
   
#print("** Reyes **\n")
#reyB = Rey("rey blanco", "Rey", "Blanco", "Lineal y Diagonal", 1, "Lineal y Diagonal")
#reyN = Rey("rey negro", "Rey", "Negro", "Lineal y Diagonal", 1, "Lineal y Diagonal")
#print(reyN.mover())
#print(reyB.capturar())
#print("")    

#print("** Alfiles **\n")
#alfilB = Alfil("alfiles blancos", "Alfil", "Blanco", "Diagonal", 2, "Diagonal")
#alfilN = Alfil("alfiles negros", "Alfil", "Negro", "Diagonal", 2, "Diagonal")
#print(alfilN.mover())
#print(alfilB.capturar())
#print("") 
    

#print(torreN.mover())
#print(torreB.capturar())
#print("") 

#print(peonN.promo())
#print(peonN.mover())
#print(peonB.capturar())
#print(peonB.promo())
#print("") 

#print("** Dama **\n")        
#damaB = Dama("damas blancas", "Dama", "Blanco", "Lineal y Diagonal", 1, "Lineal y Diagonal")
#damaN = Dama("damas negras", "Dama", "Negro", "Lineal y Diagonal", 1, "Lineal y Diagonal")
#print(damaN.mover())
#print(damaB.capturar())
#print("") 

#print("** Caballos **\n")    
#caballoB = Caballo("caballos blancos", "Caballo", "Blanco", "L", 2, "L")
#caballoN = Caballo("caballos negros", "Caballo", "Negro", "L", 2, "L")
#print(caballoN.mover())
#print(caballoB.capturar())
#print("") 
