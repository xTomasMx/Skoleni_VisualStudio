# slovo = input("Zadejte slovo+cislo: ")

#     for i in slovo:

slovo = input(f'zadej slovo+cislo: ')
print(slovo.isalpha())
print(slovo.isdigit())
      
pismena = 0
cislice = 0
for c in slovo:
    if c.isalpha():
        pismena +=1
    if c.isdigit():
        cislice +=1

print(f'pocet pismen je {pismena} a cislic {cislice}')