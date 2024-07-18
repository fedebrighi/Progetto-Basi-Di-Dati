from app.db import execute_query

def elimina_giocatore(connection, codice_fiscale):
    query_giocatore = "DELETE FROM giocatore WHERE CodiceFiscale = %s"
    query_numero = "DELETE FROM numero WHERE CodiceFiscale = %s"
    values = (codice_fiscale,)

    try:
        execute_query(connection, query_numero, values)
        execute_query(connection, query_giocatore, values)
        connection.commit()
        return True
    except Exception as e:
        print(f"Errore durante l'eliminazione del giocatore: {e}")
        connection.rollback()
        return False
