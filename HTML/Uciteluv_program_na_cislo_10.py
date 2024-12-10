vstup = input(f'zadej 10 mistne cislo: ')
sum = 0
for i in vstup:
    if int(i)%2==0:
        rozhodnuti = 'suda'
    else:
        rozhodnuti = 'licha'
    print(f'cislice {i} je {rozhodnuti}')
    sum+=int(i)
print(f'soucet vsech cislic je {sum}')