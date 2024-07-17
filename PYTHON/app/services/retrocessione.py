from app.db import fetch_query, execute_query
from app.config import PUNTEGGIO_SOGLIA_RETROCESSIONE

def check_and_relegate_teams(connection):
    """
    Controlla tutte le squadre e rimuove quelle che hanno un punteggio inferiore alla soglia di retrocessione.

    :param connection: Connessione al database.
    """
    query_select = "SELECT id, Nome FROM squadra WHERE Punteggio < %s"
    values = (PUNTEGGIO_SOGLIA_RETROCESSIONE,)
    result = fetch_query(connection, query_select, values)
    
    if result:
        for row in result:
            squadra_id = row[0]
            squadra_nome = row[1]
            query_delete = "DELETE FROM squadra WHERE id = %s"
            execute_query(connection, query_delete, (squadra_id,))
            print(f"Squadra '{squadra_nome}' con ID {squadra_id} è stata retrocessa.")
