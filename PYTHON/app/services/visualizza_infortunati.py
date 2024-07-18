from app.db import fetch_query

def get_giocatori_infortunati(connection):
    query = "SELECT Nome, NomeSquadra, Infortunio FROM giocatore WHERE Infortunio = 'Infortunato'"
    
    try:
        return fetch_query(connection, query)
    except Exception as e:
        print(f"Errore durante il recupero dei giocatori infortunati: {e}")
        return []
