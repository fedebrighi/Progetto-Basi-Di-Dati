from app.db import execute_query

def registra_infortunio(connection, id_giocatore, descrizione, durata_giorni):
    """
    Registra un infortunio per un giocatore nel database.

    :param connection: Connessione al database.
    :param id_giocatore: ID del giocatore infortunato.
    :param descrizione: Descrizione dell'infortunio.
    :param durata_giorni: Durata prevista dell'assenza in giorni.
    """
    query = f"""
    INSERT INTO infortuni (id_giocatore, descrizione, durata_giorni)
    VALUES ({id_giocatore}, '{descrizione}', {durata_giorni})
    """
    execute_query(connection, query)

def aggiorna_infortunio(connection, id_infortunio, recupero):
    """
    Aggiorna lo stato di recupero di un infortunio.

    :param connection: Connessione al database.
    :param id_infortunio: ID dell'infortunio da aggiornare.
    :param recupero: Stato di recupero (True o False).
    """
    query = f"""
    UPDATE infortuni
    SET recupero = {recupero}
    WHERE id = {id_infortunio}
    """
    execute_query(connection, query)

def get_infortuni_giocatore(connection, id_giocatore):
    """
    Recupera tutti gli infortuni di un determinato giocatore.

    :param connection: Connessione al database.
    :param id_giocatore: ID del giocatore.
    :return: Lista di infortuni.
    """
    query = f"SELECT * FROM infortuni WHERE id_giocatore = {id_giocatore}"
    return fetch_query(connection, query)

def get_tutti_infortuni(connection):
    """
    Recupera tutti gli infortuni registrati nel database.

    :param connection: Connessione al database.
    :return: Lista di infortuni.
    """
    query = "SELECT * FROM infortuni"
    return fetch_query(connection, query)
