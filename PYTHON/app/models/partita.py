class Partita:
    def __init__(self, id, id_squadra_casa, id_squadra_ospite, id_arbitro, stadio, data, punteggio_casa=0, punteggio_ospite=0):
        self.id = id
        self.id_squadra_casa = id_squadra_casa
        self.id_squadra_ospite = id_squadra_ospite
        self.id_arbitro = id_arbitro
        self.stadio = stadio
        self.data = data
        self.punteggio_casa = punteggio_casa
        self.punteggio_ospite = punteggio_ospite
