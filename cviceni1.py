def pozdrav(jmeno):
    text = f"Ahoj, {jmeno}!"
    return text

def vetsi_nez_tri(cislo):
    if cislo > 3:
        print(f"Cislo {cislo} je vetsi nez 3")
    else:
        print(f"Cislo {cislo} je mensi nebo rovno 3")

# Tato funkce overi, zda je cislo delitelne 3,
# pokud ano vypise "je delitelne", pokud ne "neni delitelne"
def delitelne_tremi(cislo):
    if cislo % 3 == 0:
        print(f"Cislo {cislo} je delitelne tremi")
    else:
        print(f"Cislo {cislo} neni delitelne tremi")


if __name__ == "__main__":
    # a = 1
    # b = 2

    # c = a + b
    # print(c)
    
    #print(pozdrav("Yaroslav"))
    #vetsi_nez_tri(2)
    # hodnota = input("Zadej cislo: ")
    # hodnota = int(hodnota)
    # vetsi_nez_tri(hodnota)
    hodnota = input("Zadej cislo: ")
    hodnota = int(hodnota)
    delitelne_tremi(hodnota)
