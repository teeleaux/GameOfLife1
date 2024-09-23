
matrise = [[1,3,9,4],
           [2,1,5,8],
           [7,6,3,0]]

rad = 3 #3 lister
#len(matrise) kunne også funket
kol = 4 #4 kolonner inni listene
#len(matrise[0]) gir meg lengden på antallet elementer i liste

#vi vil gjennom og skifte disse tall i listene til 0
#range(rad) = # 0 1 2
for r in range(rad): #BRUK RANGE ikke len
    #teller = 0
    #while teller < kol:
    #range(kol) = # 0 1 2 3
    for k in range(kol):
        matrise[r][k] = 0 # her trenger vi både i og j for å hente alle indekser inni de nøstet listene
    #    teller += 1

    #fyll med tilfeldelige celler




print(matrise)

# bruk i in range for tegnebiten og for rader og kolonner
# self._kolonner
#self._rader



#tengedelen
#for each for løkke, kan ikke endre det som ligger der
for liste in matrise:
    for tall in liste:
        print(tall, end=" ") #end = " " dette gir oss mulighet å printe listene med mellomrom og ikke på new line
    print()


#på sett naboer sjekk hver eneste rute rundt naboer

#bruker rad og kolonne for å hente duden
#rad - 1

#def sett_nabo(self, rad, kol):
