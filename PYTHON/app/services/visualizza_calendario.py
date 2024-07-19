from app.db import fetch_query

def get_partite(connection):
    query = "SELECT NomeCasa, NomeOspite, Giorno, Mese, Anno FROM partita"
    return fetch_query(connection, query)
