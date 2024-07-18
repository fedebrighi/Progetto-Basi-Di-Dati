from app.db import fetch_query

def get_giocatori_espulsi(connection):
    query = "SELECT Nome,Cognome, NomeSquadra, Espulsione FROM giocatore WHERE Espulsione = 'Espulso'"
    
    try:
        return fetch_query(connection, query)
    except Exception as e:
        print(f"Errore durante il recupero dei giocatori espulsi: {e}")
        return []
