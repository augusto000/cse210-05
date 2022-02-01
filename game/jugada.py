from game.ocultador import Ocultador
from game.warmer import Warmer
from game.colder import Colder
class Jugada:
    
    def __init__(self):
        self._name="Marcos"
        self._location = 0
        self._isPlaying = True 
        #self._n=0       
        self._isFirstRound=True
        self._r2=0

    def setName(self, name):        
        self._name = name
        print()

    def getName(self):
        return f"..get ready {self._name}"

    def inputs(self):
        n = input("Input your Name : ")
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
        #print(n)
        ocultador = Ocultador()   
        #set the hidding number       
        ocultador.setOcultador()
        j=ocultador.getOcultador()
        colder = Colder()
        warmer = Warmer()
        
        while self._isPlaying:                    
            if self._isFirstRound:
                print(j)  
                #set the number that get closer
                ot = int(input("Enter a Location [1-1000] : "))
                jugada.setLocation(ot)
                ot = jugada.getLocation()
                
                self._isFirstRound=False
                #ot es el numero ingresado por el usuario
                #j es el numero aleatorio de 1 al 1000.
                r1 = j - ot
                self._r2 = r1

                if r1 == 0:
                    print("son iguales..")
                    print("Me pillaste...The Game is Over !!")
                    exit()
                elif r1 > j  :
                    print(r1)
                    colder.outPutcolder()
                elif r1 < j:
                    colder.outPutColder()
            
            else:
                print("Segunda vuelta")
                print(j)  
                #set the number that get closer
                ot = int(input("Enter a Location [1-1000] : "))
                jugada.setLocation(ot)
                ot = jugada.getLocation()
                #ot es el numero ingresado por el usuario
                #j es el numero aleatorio de 1 al 1000.
                r1 = j - ot
                    
                if r1 == 0:
                    print("You Found me!")
                    exit()
                elif r1 >= self._r2 :
                    colder.outPutColder()
                elif r1 <= self._r2:
                    warmer.outPutWarmer()

jugada = Jugada()            

         




