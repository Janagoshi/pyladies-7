#Ukol - pridej podminku, ze pokud uzivatel nezada cislo (ale napr. retezec),
#tak mu program napise, ze pro obsah je potreba cislo a bude se ptat dal,
#dokud opravdu nedostane cislo.

while True:
    try:
        strana = float(input('Zadej stranu čtverce v centimetrech: '))
    except ValueError:
        print("Zadej prosim cislo.")
    else:
        if strana <= 0:
            print('Delka strany musi byt kladne cislo!')
        else:
            break

print("Obsah ctverce je {}".format(strana*strana))
