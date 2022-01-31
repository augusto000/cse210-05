from game.ocultador import Ocultador
from game.warmer import Warmer
from game.colder import Colder
class Jugada:
    
    def __init__(self):
        self._name=""
        self._location = 0
        self._isPlaying = True 
       # self._n=0       

    def setName(self, name):        
        self._name = name
        print()

    def getName(self):
        return f"..get ready {self._name}"

    def inputs(self):
        n = input("Ingrese Datos del Jugador : ")
        return n

    def setLocation(self, num):
        self._location = num

    def getLocation(self):
        return self._location    
   
    
    def setIsPlaying(self, state):
        self._isPlaying=state
                
    def start_game(self):
        
        n=jugada.inputs()
        jugada.setName(n)
        n=jugada.getName()
        print(n)  
        while self._isPlaying:                    
            #ocultador is the hidding number
            ocultador = Ocultador()   
            #set the hidding number       
            ocultador.setOcultador()
            j=ocultador.getOcultador()

            
            #set the number that get closer
            ot = int(input("Enter a Location [1-1000] : "))
            jugada.setLocation(ot)
            ot = jugada.getLocation()

            if ot == j:
                print("son iguales..")
                print("Me pillaste...The Game is Over !!")
                exit()
            else:
                self.start_game()

jugada = Jugada()            

         




