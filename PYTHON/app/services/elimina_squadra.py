from app.db import fetch_query, execute_query

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
    
    # Elimina la squadra dal database
    query_delete = "DELETE FROM squadra WHERE Nome = %s"
    values_delete = (nome_squadra,)
    execute_query(connection, query_delete, values_delete)
    connection.commit()

    # Aggiorna la PosClassifica per tutte le squadre
    update_classifica(connection)

def update_classifica(connection):
    """
    Aggiorna la PosClassifica delle squadre in base al punteggio.
    """
    query = """
    SET @pos = 0;
    UPDATE squadra
    SET PosClassifica = (@pos := @pos + 1)
    ORDER BY Punteggio DESC, Nome ASC;
    """
    execute_query(connection, query)
    connection.commit()
