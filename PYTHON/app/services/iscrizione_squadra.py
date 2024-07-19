from app.db import fetch_query, execute_query


def iscrizione_squadra(connection, nome_squadra, anno_squadra, citta_squadra, quota_squadra, trofei_vinti):
    """
    Iscrive una nuova squadra nel database.
    
    :param connection: Connessione al database.
    :param nome_squadra: Nome della squadra.
    :param anno_squadra: Anno di fondazione della squadra.
    :param citta_squadra: Città di riferimento della squadra.
    :param quota_squadra: Quota di iscrizione della squadra.
    :param trofei_vinti: Numero di trofei vinti dalla squadra.
    """
    # Recupera la posizione massima in classifica
    query_max_posizione = "SELECT MAX(PosClassifica) FROM squadra"
    result = fetch_query(connection, query_max_posizione)
    max_posizione = result[0][0] if result[0][0] is not None else 0
    nuova_posizione = int(max_posizione) + 1

    query = """
    INSERT INTO squadra (Nome, AnnoFondazione, CittaRiferimento, Quota_Iscrizione, TrofeiVinti, Punteggio, PosClassifica)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    PUNTEGGIO_INIZIALE = 10
    values = (nome_squadra, anno_squadra, citta_squadra, quota_squadra, trofei_vinti, PUNTEGGIO_INIZIALE, nuova_posizione)
    try:
        execute_query(connection, query, values)
        connection.commit()
        print(f"Squadra {nome_squadra} iscritta con successo.")
    except Exception as e:
        print(f"Errore durante l'iscrizione della squadra: {e}")
