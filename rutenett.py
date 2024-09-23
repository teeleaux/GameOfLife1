from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = int(rader)
        self._ant_kolonner = int(kolonner)
        self._rutenett = []
        self._lag_tomt_rutenett()

    def _lag_tomt_rutenett(self):
        #holder telling mens vi itirerer gjennom ant rad
        teller = 0

        while teller < self._ant_rader:
            self._rutenett.append(self._lag_tom_rad())
            teller += 1
        return self._rutenett

    def _lag_tom_rad(self):
        #Metoden _lag_tom_rad som bare lager en enkel liste med like
        #mange None-verdier som det skal være kolonner,
        #og returnerer denne listen.

        tom_liste = [] #oppretter tom liste å append til
        #itirerer gjennom antall kolonnet og appen tom liste
        while len(tom_liste) < self._ant_kolonner:
            tom_liste.append(None)
        #returnerer tom liste
        return tom_liste


    def fyll_med_tilfeldige_celler(self):
        #returnere og fyller med tilfeldige celler
        #itirerer gjennom matrise
        for r in range(self._ant_rader):
            for k in range(self._ant_kolonner):
                #lager celle objekt og setter inni matrisen
                self._rutenett[r][k] = self.lag_celle(r,k)
                #if sjekk for randint som setter celle til levende
                randTall = randint(0,2)
                if randTall == 2:
                    self._rutenett[r][k].sett_levende()
        return self._rutenett


    def lag_celle(self, rad, kol):
        #tar inn rad og kol og lager en celle
        celle = Celle()
        return celle


    def hent_celle(self, rad, kol):
        #tar inn rad og kol og henter en celle
        if rad in range(self._ant_rader):
            if kol in range(self._ant_kolonner):
                return self._rutenett[rad][kol]
            else:
                return None

    def tegn_rutenett(self):
        #itirerer gjennom matrise med nøstet for løkke
        for liste in self._rutenett:
            for tall in liste:
                print(tall.hent_status_tegn(), end=" ") #end = " " dette gir oss mulighet å printe listene med mellomrom og ikke på new line
            print()

        print()

    def _sett_naboer(self, rad, kol):
        #lager en tom liste for naboer
        #sette naboer og sjekk opp mot celle så legg_til_nabo

        celle = self.hent_celle(rad,kol)

        nabo1 = self.hent_celle(rad-1, kol-1)
        nabo2 = self.hent_celle(rad-1, kol)
        nabo3 = self.hent_celle(rad-1, kol+1)
        nabo4 = self.hent_celle(rad, kol-1)
        nabo5 = self.hent_celle(rad, kol+1)
        nabo6 = self.hent_celle(rad+1, kol-1)
        nabo7 = self.hent_celle(rad+1,kol)
        nabo8 = self.hent_celle(rad+1, kol+1)
        naboer = [nabo1, nabo2, nabo3, nabo4, nabo5, nabo6, nabo7, nabo8]

        for nabo in naboer:
            if nabo != None:
                celle.legg_til_nabo(nabo)
                
        # Bruker for-løkke over isteden
        # nabo1 = self.hent_celle(rad-1, kol-1)
        # if nabo1 is not None:
        #     celle.legg_til_nabo(nabo1)
        #
        # nabo2 = self.hent_celle(rad-1, kol)
        # if nabo2 != None:
        #     celle.legg_til_nabo(nabo2)
        #
        # nabo3 = self.hent_celle(rad-1, kol+1)
        # if nabo3 != None:
        #     celle.legg_til_nabo(nabo3)
        #
        # nabo4 = self.hent_celle(rad, kol-1)
        # if nabo4 != None:
        #     celle.legg_til_nabo(nabo4)
        #
        # nabo5 = self.hent_celle(rad, kol+1)
        # if nabo5 != None:
        #     celle.legg_til_nabo(nabo5)
        #
        # nabo6 = self.hent_celle(rad+1, kol-1)
        # if nabo6 != None:
        #     celle.legg_til_nabo(nabo6)
        #
        # nabo7 = self.hent_celle(rad+1,kol)
        # if nabo7 != None:
        #     celle.legg_til_nabo(nabo7)
        #
        # nabo8 = self.hent_celle(rad+1, kol+1)
        # if nabo8 != None:
        #     celle.legg_til_nabo(nabo8)

    def koble_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self._sett_naboer(rad, kol)

    def hent_alle_celler(self):
        # hent_alle_celler skal returnere en enkel liste (ikke nøstet)
        # med alle instanser av klassen Celle i et rutenett.
        liste_celler = []

        for r in range(self._ant_rader):
            for k in range(self._ant_kolonner):
                celle = self.hent_celle(r,k)
                liste_celler.append(celle)

        return liste_celler

    def antall_levende(self):
        #bruk return her eller for løkke for å itirere gjennom rutenett
        #return self.tell_levende_naboer(self)
        teller = 0

        for r in range(self._ant_rader):
            for k in range(self._ant_kolonner):
                if self.hent_celle(r,k).er_levende():
                    teller += 1
        return teller
