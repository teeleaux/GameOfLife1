class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0

    def sett_doed(self):
        self._status = "doed"

    def sett_levende(self):
        self._status = "levende"

    def er_levende(self):
        return self._status == "levende"

    def hent_status_tegn(self):
        if self._status == "levende":
            return "O"
        elif self._status == "doed":
            return "."

    def legg_til_nabo(self, nabo):
        return self._naboer.append(nabo)

    def tell_levende_naboer(self):
        #variabel å telle på nye levende naboer
        ny_nabo = 0
        for nabo in self._naboer:
            if nabo._status == "levende":
                ny_nabo += 1
        self._ant_levende_naboer = ny_nabo
        return self._ant_levende_naboer

    def oppdater_status(self):
        #bruk if sjekk for reglene som står i oppgaven
        if self._status == "levende":
            if self._ant_levende_naboer < 2:
                self._status = "doed"
            if self._ant_levende_naboer == 2 or 3:
                self._status = "levende"
            if self._ant_levende_naboer > 3:
                self._status = "doed"
        elif self._status == "doed":
            if self._ant_levende_naboer == 3:
                self._status = "levende"
