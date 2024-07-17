from app.db import fetch_query
from app.models.squadra import Squadra

def get_squadre(connection):
    """
    Recupera tutte le squadre dal database.
    
    :param connection: Connessione al database.
    :return: Lista di squadre.
    """
    query = "SELECT Nome, AnnoFondazione, CittaRiferimento, TrofeiVinti, Quota_Iscrizione, Punteggio FROM squadra"
    result = fetch_query(connection, query)
    print(f"Squadre recuperate dal database: {result}")  # Debug: stampa i risultati della query
    return result
