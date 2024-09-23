from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = Rutenett(self._ant_rader, self._ant_kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()

    def tegn(self):

        self._rutenett.tegn_rutenett()
        print('Generasjonsnummer: ', self._generasjonsnummer,' - Antall levende celler: ', self._rutenett.antall_levende())
        print()

    def oppdatering(self):
        #bruk eksisterende metoder
#       a. Gå gjennom alle celler i rutenettet og
#       telle levende naboer for hver celle
        celler = self._rutenett.hent_alle_celler()

        for celle in celler:
            celle.tell_levende_naboer()
#       b. Gå gjennom alle celler i rutenettet på nytt,
        #og oppdatere status på hver celle
        for celle in celler:
            celle.oppdater_status()
#       c. Til sist må du huske å oppdatere telleren for antall generasjoner.
        self._generasjonsnummer += 1
