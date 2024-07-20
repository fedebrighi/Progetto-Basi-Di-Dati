from app.db import fetch_query

def get_classifica(connection):
    """
    Recupera la classifica delle squadre dal database.
    
    :param connection: Connessione al database.
    :return: Lista di squadre in classifica.
    """
    query1 = "SET @row_number = 0;"
    query = """
    SELECT Nome, Punteggio, (@row_number := @row_number + 1) AS PosClassifica
    FROM squadra ORDER BY 
    Punteggio DESC;
    """
    fetch_query(connection, query1)
    result = fetch_query(connection, query)
    print(f"Classifica recuperata dal database: {result}")  # Debug: stampa i risultati della query
    return result
