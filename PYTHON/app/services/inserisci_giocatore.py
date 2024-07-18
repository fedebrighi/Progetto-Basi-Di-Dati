from app.db import execute_query

def inserisci_giocatore(connection, codice_fiscale, nome, cognome, data_nascita, nazionalita, stipendio, infortunio, espulsione, nome_squadra, numero, ruolo):
    query_giocatore = """
    INSERT INTO giocatore (CodiceFiscale, Nome, Cognome, DataNascita, Nazionalita, Stipendio, Infortunio, Espulsione, NomeSquadra)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values_giocatore = (codice_fiscale, nome, cognome, data_nascita, nazionalita, stipendio, infortunio, espulsione, nome_squadra)

    query_numero = """
    INSERT INTO numero (CodiceFiscale, NomeSquadra, Numero, Ruolo)
    VALUES (%s, %s, %s, %s)
    """
    values_numero = (codice_fiscale, nome_squadra, numero, ruolo)

    try:
        execute_query(connection, query_giocatore, values_giocatore)
        execute_query(connection, query_numero, values_numero)
        connection.commit()
        return True
    except Exception as e:
        print(f"Errore durante l'inserimento del giocatore: {e}")
        connection.rollback()
        return False
