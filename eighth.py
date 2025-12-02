def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    binarni_cislo_str = str(binarni_cislo)
    decimalna_hodnota = 0
    mocnina = 0
    for cislo in binarni_cislo_str:
        decimalna_hodnota += int(cislo) *(2 ** (len(binarni_cislo_str) - mocnina - 1))
        mocnina += 1
    if binarni_cislo_str == "0":
        return 0
    else:
        return decimalna_hodnota


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128


if __name__ == "__main__":
    print(bin_to_dec("1100100"))
    print(bin_to_dec(1100101))