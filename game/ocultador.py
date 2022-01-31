import random
class Ocultador:
    def __init__(self):
        self._num=0
    
    def setOcultador(self):
        #es el numero a buscar
        self._num = random.randint(1, 1000)
        
    def getOcultador(self):
        #es el numero a buscar
        return self._num




