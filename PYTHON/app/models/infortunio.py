class Infortunio:
    def __init__(self, id, id_giocatore, descrizione, durata_giorni, recupero=False):
        self.id = id
        self.id_giocatore = id_giocatore
        self.descrizione = descrizione
        self.durata_giorni = durata_giorni
        self.recupero = recupero
