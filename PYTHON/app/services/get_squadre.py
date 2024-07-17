from app.db import fetch_query
from app.models.squadra import Squadra

def get_squadre(connection):
    """
    Recupera tutte le squadre dal database e le converte in oggetti Squadra.

    :param connection: Connessione al database.
    :return: Lista di oggetti Squadra.
    """
    query = "SELECT Nome, AnnoFondazione, CittaRiferimento, TrofeiVinti, Quota_Iscrizione, Punteggio, PosClassifica FROM squadra"
    print(f"Eseguendo la query: {query}")
    result = fetch_query(connection, query)
    squadre = []
    for row in result:
        squadra = Squadra(
            nome=row[0],
            annofondazione=row[1],
            cittariferimento=row[2],
            trofeivinti=row[3],
            quotaiscrizione=row[4],
            punteggio=row[5],
            posclassifica=row[6]
        )
        squadre.append(squadra)
    return squadre
