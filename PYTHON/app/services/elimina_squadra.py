from app.db import fetch_query, execute_query

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

def elimina_squadra(connection, nome_squadra):
    """
    Elimina una squadra dal database e aggiorna la classifica.

    :param connection: Connessione al database.
    :param nome_squadra: Nome della squadra da eliminare.
    """
    # Verifica se la squadra esiste
    query_check = "SELECT COUNT(*) FROM squadra WHERE Nome = %s"
    values_check = (nome_squadra,)
    result = fetch_query(connection, query_check, values_check)
    
    if result[0][0] == 0:
        print(f"Errore: La squadra '{nome_squadra}' non esiste nel database.")
        return
    
    try:
        cursor = connection.cursor()

        # Elimina i giocatori associati alla squadra
        query_get_giocatori = "SELECT CodiceFiscale FROM giocatore WHERE NomeSquadra = %s"
        cursor.execute(query_get_giocatori, (nome_squadra,))
        giocatori = cursor.fetchall()
        
        for giocatore in giocatori:
            elimina_giocatore(connection, giocatore[0])

        # Elimina le partite associate alla squadra
        query_delete_partite_casa = "DELETE FROM partita WHERE NomeCasa = %s"
        cursor.execute(query_delete_partite_casa, (nome_squadra,))

        query_delete_partite_ospite = "DELETE FROM partita WHERE NomeOspite = %s"
        cursor.execute(query_delete_partite_ospite, (nome_squadra,))

        # Elimina la squadra dal database
        query_delete = "DELETE FROM squadra WHERE Nome = %s"
        cursor.execute(query_delete, (nome_squadra,))

        # Aggiorna la PosClassifica per tutte le squadre
        update_classifica(connection)
        
        connection.commit()
        cursor.close()
        print(f"Squadra '{nome_squadra}' eliminata con successo.")
    except Exception as e:
        connection.rollback()
        print(f"Errore durante l'eliminazione della squadra '{nome_squadra}': {e}")

def update_classifica(connection):
    """
    Aggiorna la PosClassifica delle squadre in base al punteggio.
    """
    query_init = "SET @pos = 0;"
    query_update = """
    UPDATE squadra
    SET PosClassifica = (@pos := @pos + 1)
    ORDER BY Punteggio DESC;
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query_init)
        cursor.execute(query_update)
        connection.commit()
        cursor.close()
        print("Classifica aggiornata con successo.")
    except Exception as e:
        print(f"Errore durante l'aggiornamento della classifica: {e}")
        connection.rollback()
