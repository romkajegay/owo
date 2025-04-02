while True:
    cislo1 = int(input("Zadej první číslo:"))
    cislo2 = int(input("Zadej druhý číslo:"))
    
    akt = (input("Zadej co chceš s čísly dělat: Násobení, Dělení, Sčítaní nebo Odčítání:"))

    if akt == "Násobení":
        Nasobeni = cislo1 * cislo2
        print("výsledek vaší rovnice se bude rovnat", Nasobeni)

    if akt == "Dělení":
        Deleni = cislo1 / cislo2
        print("výsledek vaší rovnice se bude rovnat", Deleni) 

    if akt == "Sčítání":
        scitani = cislo1 + cislo2
        print("výsledek vaší rovnice se bude rovnat", scitani) 

    if akt == "Odčítání":
        odcitani = cislo1 - cislo2
        print("výsledek vaší rovnice se bude rovnat", odcitani) 

    print("Pokud nechcete pokračovat napište exit")
    bye=int(input("Pokud nechcete pokračovat napište exit"))
    if bye=="exit":
        break