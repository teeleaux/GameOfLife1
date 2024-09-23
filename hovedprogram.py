from verden import Verden

def hovedprogram():

    print('Vi skal spille spill!')
    rad = int(input('Hvor mange rad skal brettet ha?: '))
    kol = int(input('Hvor mange kolonner skal brettet ha?: '))

    brett = Verden(rad, kol)

    brett.tegn()

    svar = input('Tast "q" hvis du vil slutte å spille.\nEller trykke ENTER hvis du vil fortsette: ').lower()

    while svar == "":
        brett.oppdatering()
        brett.tegn()
        svar = input('Tast "q" hvis du vil slutte å spille.\nEller trykke ENTER hvis du vil fortsette: ').lower()

# starte hovedprogrammet
hovedprogram()
