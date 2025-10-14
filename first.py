def sudy_nebo_lichy(cislo):
    """
    Upravte funkci tak, aby vypisovala, zda je cislo sude nebo liche
    """
    # Úprava funkce sudy_nebo_lichy
    # Nejprve zjistíme, zda je číslo dělitelné dvěma beze zbytku.
    # Pokud ano, je sudé, jinak je liché.
    if cislo % 2 == 0:
        print(f"Čislo {cislo} je sudé") 
    else:
        print(f"Čislo {cislo} je liché")


if __name__ == "__main__":
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)