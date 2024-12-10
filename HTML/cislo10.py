def zjisti_sudou_lichou(cislice):
    if cislice % 2 == 0:
        return "sudá"
    else:
        return "lichá"

# Uživatelský vstup
cislo = input("Zadejte číslo o délce 10 číslic: ")

# Kontrola, zda uživatel zadal číslo o správné délce
if len(cislo) != 10 or not cislo.isdigit():
    print("Chyba: Musíte zadat číslo o délce 10 číslic.")
else:
    soucet = 0
    
    for i in cislo:
        cislice = int(i)  # Převede číslici na integer
        typ = zjisti_sudou_lichou(cislice)
        print(f"Číslice {cislice} je {typ}.")
        soucet += cislice

    print(f"Součet všech číslic je: {soucet}")