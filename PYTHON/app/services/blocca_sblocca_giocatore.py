from app.db import execute_query

def blocca_sblocca_giocatore(connection, codice_fiscale, stato_espulsione):
    query = "UPDATE giocatore SET Espulsione = %s WHERE CodiceFiscale = %s"
    values = (stato_espulsione, codice_fiscale)

    try:
        execute_query(connection, query, values)
        connection.commit()
        return True
    except Exception as e:
        print(f"Errore durante l'aggiornamento dello stato di espulsione: {e}")
        connection.rollback()
        return False
