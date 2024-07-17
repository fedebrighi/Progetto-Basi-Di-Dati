from app.db import fetch_query

def get_classifica(connection):
    """
    Recupera la classifica delle squadre dal database.
    
    :param connection: Connessione al database.
    :return: Lista di squadre in classifica.
    """
    query = "SELECT Nome, Punteggio, PosClassifica FROM squadra ORDER BY Punteggio DESC, PosClassifica ASC"
    result = fetch_query(connection, query)
    print(f"Classifica recuperata dal database: {result}")  # Debug: stampa i risultati della query
    return result
