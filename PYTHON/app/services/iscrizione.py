from app.db import fetch_query, execute_query
from app.config import PUNTEGGIO_SOGLIA_RETROCESSIONE

def get_max_posizione_classifica(connection):
    """
    Recupera la posizione massima in classifica dal database.

    :param connection: Connessione al database.
    :return: Posizione massima in classifica.
    """
    query = "SELECT MAX(PosClassifica) FROM squadra"
    result = fetch_query(connection, query)
    max_posizione = result[0][0] if result[0][0] is not None else 0
    return int(max_posizione)

def iscrizione_squadra(connection, nome_squadra, anno_squadra, citta_squadra, quota_squadra, trofei_vinti):
    """
    Iscrive una nuova squadra e la mette all'ultima posizione di classifica con un punteggio iniziale adeguato.

    :param connection: Connessione al database.
    :param nome_squadra: Nome della squadra.
    :param anno_squadra: Anno di fondazione della squadra.
    :param citta_squadra: Città di riferimento della squadra.
    :param quota_squadra: Quota di iscrizione della squadra.
    :param trofei_vinti: Numero di trofei vinti dalla squadra.
    """
    # Recupera la posizione massima in classifica
    max_posizione = get_max_posizione_classifica(connection)
    nuova_posizione = max_posizione + 1

    # Imposta il punteggio iniziale ad almeno la soglia di retrocessione
    punteggio_iniziale = PUNTEGGIO_SOGLIA_RETROCESSIONE

    query = """
    INSERT INTO squadra (Nome, AnnoFondazione, CittaRiferimento, Quota_Iscrizione, Punteggio, PosClassifica, TrofeiVinti)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (nome_squadra, anno_squadra, citta_squadra, quota_squadra, punteggio_iniziale, nuova_posizione, trofei_vinti)
    execute_query(connection, query, values)
