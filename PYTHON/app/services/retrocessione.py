from app.db import fetch_query, execute_query

def retrocessione_squadre(connection):
    """
    Elimina tutte le squadre con meno di 4 punti dal database e aggiorna la classifica.

    :param connection: Connessione al database.
    """
    query_select = "SELECT Nome FROM squadra WHERE Punteggio < 4"
    squadre_da_retrocedere = fetch_query(connection, query_select)
    
    try:
        cursor = connection.cursor()
        
        for squadra in squadre_da_retrocedere:
            nome_squadra = squadra[0]
            print(f"Retrocedendo la squadra: {nome_squadra}")

            # Elimina i giocatori associati alla squadra
            query_select_giocatori = "SELECT CodiceFiscale FROM giocatore WHERE NomeSquadra = %s"
            giocatori = fetch_query(connection, query_select_giocatori, (nome_squadra,))
            for giocatore in giocatori:
                codice_giocatore = giocatore[0]

                # Elimina dal mercato giocatori e dalle tabelle correlate
                query_delete_tramite = "DELETE FROM tramite WHERE CodiceGiocatore = %s"
                cursor.execute(query_delete_tramite, (codice_giocatore,))

                query_delete_mercato = "DELETE FROM mercato_giocatori WHERE CodiceGiocatore = %s"
                cursor.execute(query_delete_mercato, (codice_giocatore,))

                # Elimina il giocatore
                query_delete_numero = "DELETE FROM numero WHERE CodiceFiscale = %s"
                cursor.execute(query_delete_numero, (codice_giocatore,))

                query_delete_giocatore = "DELETE FROM giocatore WHERE CodiceFiscale = %s"
                cursor.execute(query_delete_giocatore, (codice_giocatore,))

            # Elimina gli allenatori associati alla squadra
            query_select_allenatori = "SELECT CodiceFiscale FROM allenatore WHERE All_Nome = %s"
            allenatori = fetch_query(connection, query_select_allenatori, (nome_squadra,))
            for allenatore in allenatori:
                codice_allenatore = allenatore[0]

                # Elimina il personale associato all'allenatore
                query_delete_staff = "DELETE FROM staff WHERE CodiceAll = %s"
                cursor.execute(query_delete_staff, (codice_allenatore,))

                # Elimina l'allenatore
                query_delete_allenatore = "DELETE FROM allenatore WHERE CodiceFiscale = %s"
                cursor.execute(query_delete_allenatore, (codice_allenatore,))

            # Elimina le supervisioni associate alle partite della squadra
            query_select_partite = "SELECT CodicePartita FROM partita WHERE NomeCasa = %s OR NomeOspite = %s"
            partite = fetch_query(connection, query_select_partite, (nome_squadra, nome_squadra))
            for partita in partite:
                codice_partita = partita[0]
                query_delete_supervisione = "DELETE FROM supervisione WHERE CodicePartita = %s"
                cursor.execute(query_delete_supervisione, (codice_partita,))

            # Elimina le partite associate alla squadra
            query_delete_partite_casa = "DELETE FROM partita WHERE NomeCasa = %s"
            cursor.execute(query_delete_partite_casa, (nome_squadra,))

            query_delete_partite_ospite = "DELETE FROM partita WHERE NomeOspite = %s"
            cursor.execute(query_delete_partite_ospite, (nome_squadra,))

            # Elimina la squadra
            query_delete_squadra = "DELETE FROM squadra WHERE Nome = %s"
            cursor.execute(query_delete_squadra, (nome_squadra,))

            print(f"Squadra '{nome_squadra}' eliminata con successo.")

        # Aggiorna la PosClassifica per tutte le squadre
        update_classifica(connection)
        
        connection.commit()
        cursor.close()
        print(f"Squadre retrocesse: {', '.join([squadra[0] for squadra in squadre_da_retrocedere])}")
    except Exception as e:
        connection.rollback()
        print(f"Errore durante l'eliminazione della squadra: {e}")

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
