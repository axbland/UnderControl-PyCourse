from Peones import Peon
from Torres import Torre
from Alfiles import Alfil
from Caballos import Caballo
from Dama import Dama
from Rey import Rey

print("** Reyes **\n")
reyB = Rey("rey blanco", "Rey", "Blanco", "Lineal y Diagonal", 1, "Lineal y Diagonal")
reyN = Rey("rey negro", "Rey", "Negro", "Lineal y Diagonal", 1, "Lineal y Diagonal")
print(reyN.mover())
print(reyB.capturar())
print("")    

print("** Alfiles **\n")
alfilB = Alfil("alfiles blancos", "Alfil", "Blanco", "Diagonal", 2, "Diagonal")
alfilN = Alfil("alfiles negros", "Alfil", "Negro", "Diagonal", 2, "Diagonal")
print(alfilN.mover())
print(alfilB.capturar())
print("") 
    
print("** Torres **\n")    
torreB = Torre("torres blancas", "Torre", "Blanco", "Lineal", 2, "Lineal")
torreN = Torre("torres negros", "Torre", "Negro", "Lineal", 2, "Lineal")
print(torreN.mover())
print(torreB.capturar())
print("") 

print("** Peones **\n")    
peonB = Peon("peones blancos", "Peon", "Blanco", "Lineal", 8, "Lineal y Al Paso")
peonN = Peon("peones negros", "Peon", "Negro", "Lineal", 8, "Lineal y Al Paso")
print(peonN.promo())
print(peonN.mover())
print(peonB.capturar())
print(peonB.promo())
print("") 

print("** Dama **\n")        
damaB = Dama("damas blancas", "Dama", "Blanco", "Lineal y Diagonal", 1, "Lineal y Diagonal")
damaN = Dama("damas negras", "Dama", "Negro", "Lineal y Diagonal", 1, "Lineal y Diagonal")
print(damaN.mover())
print(damaB.capturar())
print("") 

print("** Caballos **\n")    
caballoB = Caballo("caballos blancos", "Caballo", "Blanco", "L", 2, "L")
caballoN = Caballo("caballos negros", "Caballo", "Negro", "L", 2, "L")
print(caballoN.mover())
print(caballoB.capturar())
print("") 