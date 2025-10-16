def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    cislo = int(cislo)
    desitka = cislo // 10
    jednotka = cislo % 10
    if jednotka == 0:
        text_jednotka = "nula"
    elif jednotka == 1:
        text_jednotka = "jedna"
    elif jednotka == 2:
        text_jednotka = "dva"
    elif jednotka == 3:
        text_jednotka = "tři"
    elif jednotka == 4:
        text_jednotka = "čtyři"
    elif jednotka == 5:
        text_jednotka = "pět"
    elif jednotka == 6:
        text_jednotka = "šest"
    elif jednotka == 7:
        text_jednotka = "sedm"
    elif jednotka == 8:
        text_jednotka = "osm"
    elif jednotka == 9:
        text_jednotka = "devět"
    
    if cislo < 10:
        return text_jednotka

    if desitka == 1:
        if desitka == 1 and jednotka == 0:
            return "deset"
        elif desitka == 1 and jednotka == 1:
            return "jedenáct"
        elif desitka == 1 and jednotka == 2:
            return "dvanáct"
        elif desitka == 1 and jednotka == 3:
            return "třináct"
        elif desitka == 1 and jednotka == 4:
            return "čtrnáct"
        elif desitka == 1 and jednotka == 5:
            return "patnáct"
        elif desitka == 1 and jednotka == 6:
            return "šestnáct"
        elif desitka == 1 and jednotka == 7:
            return "sedmnáct"
        elif desitka == 1 and jednotka == 8:
            return "osmnáct"
        elif desitka == 1 and jednotka == 9:
            return "devatenáct"

    elif desitka >= 2 and desitka <= 9:
        if desitka == 2:
            text_desitka = "dvacet"
        elif desitka == 3:
            text_desitka = "třicet"
        elif desitka == 4:
            text_desitka = "čtyřicet"
        elif desitka == 5:
            text_desitka = "padesát"
        elif desitka == 6:
            text_desitka = "šedesát"
        elif desitka == 7:
            text_desitka = "sedmdesát"
        elif desitka == 8:
            text_desitka = "osmdesát"
        elif desitka == 9:
            text_desitka = "devadesát"
        else:
            text_desitka = ""
        
        if jednotka != 0:
            text_desitka += " " + text_jednotka
        return text_desitka
    
    elif cislo == 100:
        return "sto"
    else:
        return "Čislo je mimo rozsah 0-100"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)