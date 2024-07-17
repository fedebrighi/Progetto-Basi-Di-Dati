from app.db import execute_query, fetch_query

def proponi_scambio(connection, id_giocatore_offerto, id_squadra_destinazione, id_giocatore_richiesto, id_squadra_proponente):
    """
    Proponi uno scambio di giocatori tra due squadre.

    :param connection: Connessione al database.
    :param id_giocatore_offerto: ID del giocatore offerto per lo scambio.
    :param id_squadra_destinazione: ID della squadra a cui è offerto il giocatore.
    :param id_giocatore_richiesto: ID del giocatore richiesto in cambio.
    :param id_squadra_proponente: ID della squadra che propone lo scambio.
    """
    query = f"""
    INSERT INTO scambi (id_giocatore_offerto, id_squadra_destinazione, id_giocatore_richiesto, id_squadra_proponente)
    VALUES ({id_giocatore_offerto}, {id_squadra_destinazione}, {id_giocatore_richiesto}, {id_squadra_proponente})
    """
    execute_query(connection, query)

def esegui_scambio(connection, id_giocatore_offerto, id_squadra_destinazione, id_giocatore_richiesto, id_squadra_proponente):
    """
    Esegui lo scambio di giocatori tra due squadre.

    :param connection: Connessione al database.
    :param id_giocatore_offerto: ID del giocatore offerto per lo scambio.
    :param id_squadra_destinazione: ID della squadra a cui è offerto il giocatore.
    :param id_giocatore_richiesto: ID del giocatore richiesto in cambio.
    :param id_squadra_proponente: ID della squadra che propone lo scambio.
    """
    query1 = f"""
    UPDATE giocatori
    SET id_squadra = {id_squadra_destinazione}
    WHERE id = {id_giocatore_offerto}
    """
    query2 = f"""
    UPDATE giocatori
    SET id_squadra = {id_squadra_proponente}
    WHERE id = {id_giocatore_richiesto}
    """
    execute_query(connection, query1)
    execute_query(connection, query2)

def get_scambi_proposti(connection, id_squadra):
    """
    Recupera tutti gli scambi proposti da una squadra.

    :param connection: Connessione al database.
    :param id_squadra: ID della squadra proponente.
    :return: Lista di scambi proposti.
    """
    query = f"""
    SELECT * FROM scambi
    WHERE id_squadra_proponente = {id_squadra}
    """
    return fetch_query(connection, query)

def get_scambi_ricevuti(connection, id_squadra):
    """
    Recupera tutti gli scambi ricevuti da una squadra.

    :param connection: Connessione al database.
    :param id_squadra: ID della squadra destinazione.
    :return: Lista di scambi ricevuti.
    """
    query = f"""
    SELECT * FROM scambi
    WHERE id_squadra_destinazione = {id_squadra}
    """
    return fetch_query(connection, query)
