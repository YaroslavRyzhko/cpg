class Zvire:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.pocet_navstev_veterinarne = 0

    def pocet_navstev(self):
        self.pocet_navstev_veterinarne += 1

    def __str__(self):
        return f'Zvire(jmeno={self.jmeno}, navstevy={self.pocet_navstev_veterinarne})'    
    
class Pes(Zvire):
    
    def __init__(self, jmeno, rasa):
        super().__init__(jmeno)
        self.rasa = rasa
    
    def __str__(self):
        return f'Pes(jmeno={self.jmeno}, rasa={self.rasa}, navstevy={self.pocet_navstev_veterinarne})'
    
class Kocka(Zvire):
    def __init__(self, jmeno, barva):
        super().__init__(jmeno)
        self.barva = barva
        self.pocet_zivotu = 7

    def ubere_zivot(self):
        self.pocet_zivotu -= 1

    def __str__(self):
        if self.pocet_zivotu <= 0:
            return f"kocka {self.jmeno} je mrtva"
        else:
            return f"Kockajmeno={self.jmeno}, rasa={self.barva}, navstevy={self.pocet_navstev_veterinarne}, zivoty={self.pocet_zivotu})"
    

if __name__ == "__main__":
    pes1 = Pes("Ivan", "jezevcik")
    pes2 = Pes("Rex", "Labrador")
    pes3 = Pes("Max", "buldog")
    pes4 = Pes("Alik", "vlcak")
    
    print(pes1)
    print(pes2)
    print(pes3)
    print(pes4)

    kocka = Kocka("Murka", "cerna")
    kocka.ubere_zivot()

    print(kocka)