import math
from abc import ABC, abstractmethod

class Tvar(ABC):
    @abstractmethod
    def obsah(self):
        pass


class Kruh(Tvar):
    def __init__(self, polomer):
        self.polomer = polomer
    
    def obsah(self):
        return  math.pi * self.polomer * self.polomer 

class Obdenik(Tvar):
    def __init__(self, sirka, delka):
        self.sirka = sirka
        self.delka = delka

    def obsah(self):
        return self.sirka * self.delka 

class Ctvrec(Obdenik):
    def __init__(self,  delka_hrany):
        super().__init__(delka_hrany, delka_hrany)

 
        

if __name__ == "__main__":
    
    #k = Kruh(5)
    #print(k.obsah())
    tvary = [Kruh(3), Kruh(2), Obdenik(2, 5), Kruh(1), Ctvrec(5)]
    celkovy_obsah = 0
    for tvar in tvary:
        celkovy_obsah += tvar.obsah()
    
    print(round(celkovy_obsah, 2))