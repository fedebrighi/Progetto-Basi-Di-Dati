from app.db import execute_query, fetch_query

def retrocessione_squadre(connection):
    """
    Controlla tutte le squadre nel database e rimuove quelle con meno di 4 punti.
    """
    # Seleziona tutte le squadre con meno di 4 punti
    query_select = "SELECT Nome FROM squadra WHERE Punteggio < 4"
    squadre_da_retrocedere = fetch_query(connection, query_select)
    
    if squadre_da_retrocedere:
        # Elimina le squadre trovate
        query_delete = "DELETE FROM squadra WHERE Punteggio < 4"
        execute_query(connection, query_delete)
        connection.commit()
        print(f"Squadre retrocesse: {', '.join([squadra[0] for squadra in squadre_da_retrocedere])}")
        return True
    else:
        print("Nessuna squadra da retrocedere.")
        return False
