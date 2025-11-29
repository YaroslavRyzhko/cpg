

class BankovniUcet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.zustatek = 0
    
    def __str__(self):
        return f"Učet({self.jmeno}): {self.zustatek} kč"
    
    
    @property
    def zustatek(self):
        return self.__zustatek

    @zustatek.setter
    def zustatek(self, novy_zusatek):
        if novy_zusatek >= 0:
            self.__zustatek = novy_zusatek



if __name__ == "__main__":
    u = BankovniUcet("spořící")
    print(u.zustatek)
    u.zustatek = 200
    print(u)