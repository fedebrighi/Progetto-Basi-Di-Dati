from app.db import fetch_query

def get_classifica(connection):
    """
    Recupera la classifica delle squadre dal database ordinata per punteggio in modo decrescente e posizione in classifica in modo crescente.

    :param connection: Connessione al database.
    :return: Lista di tuple contenenti nome squadra, punteggio e posizione in classifica.
    """
    query = """
    SELECT Nome, Punteggio, PosClassifica 
    FROM squadra 
    ORDER BY Punteggio DESC, PosClassifica ASC
    """
    print(f"Eseguendo la query: {query}")
    return fetch_query(connection, query)

