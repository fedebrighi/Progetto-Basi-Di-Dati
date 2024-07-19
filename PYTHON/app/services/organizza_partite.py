import random
import uuid
from datetime import date
from app.db import fetch_query, execute_query

def genera_risultato_casuale():
    goal_casa = random.randint(0, 5)
    goal_ospite = random.randint(0, 5)
    return goal_casa, goal_ospite, f"{goal_casa}-{goal_ospite}"

def genera_biglietti_e_prezzo():
    biglietti = random.randint(1000, 50000)
    prezzo_biglietto = random.randint(10, 100)
    return biglietti, prezzo_biglietto

def genera_statistiche():
    pali = random.randint(0, 5)
    cartellini = random.randint(0, 5)
    return pali, cartellini

def inserisci_tabellino_statistiche(connection, codice_tabellino, goal_casa, goal_ospite, codice_staff):
    data_tab = date.today().isoformat()
    pali, cartellini = genera_statistiche()
    query = """
    INSERT INTO tabellino_statistiche (CodiceTabellino, DataTab, GoalCasa, GoalOspite, Pali, Cartellini, CodiceStaff)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (codice_tabellino, data_tab, goal_casa, goal_ospite, pali, cartellini, codice_staff)
    try:
        execute_query(connection, query, values)
        connection.commit()
        print(f"Tabellino inserito: {codice_tabellino} con data {data_tab}, GoalCasa: {goal_casa}, GoalOspite: {goal_ospite}, Pali: {pali}, Cartellini: {cartellini}, CodiceStaff: {codice_staff}")
        return True
    except Exception as e:
        print(f"Errore durante l'inserimento del tabellino: {e}")
        connection.rollback()
        return False

def inserisci_data(connection, giorno, mese, anno, codTorneo):
    query = """
    INSERT INTO data (Giorno, Mese, Anno, CodTorneo)
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE Giorno=VALUES(Giorno), Mese=VALUES(Mese), Anno=VALUES(Anno), CodTorneo=VALUES(codTorneo)
    """
    values = (giorno, mese, anno, codTorneo)
    try:
        execute_query(connection, query, values)
        connection.commit()
        print(f"Data inserita o già esistente: {giorno}-{mese}-{anno}")
        return True
    except Exception as e:
        print(f"Errore durante l'inserimento della data: {e}")
        connection.rollback()
        return False

def aggiorna_punteggio_squadra(connection, nome_squadra, punteggio_da_aggiungere):
    query = """
    UPDATE squadra
    SET Punteggio = Punteggio + %s
    WHERE Nome = %s
    """
    values = (punteggio_da_aggiungere, nome_squadra)
    try:
        execute_query(connection, query, values)
        connection.commit()
        print(f"Punteggio aggiornato per {nome_squadra}: {punteggio_da_aggiungere}")
    except Exception as e:
        print(f"Errore durante l'aggiornamento del punteggio per {nome_squadra}: {e}")
        connection.rollback()

def inserisci_partita(connection, giorno, mese, anno, squadra_casa, squadra_trasferta, codice_stadio, codice_staff, cod_torneo):
    goal_casa, goal_ospite, risultato = genera_risultato_casuale()
    codice_partita = str(uuid.uuid4())[:8]
    codice_tabellino = str(uuid.uuid4())[:8]
    biglietti, prezzo_biglietto = genera_biglietti_e_prezzo()

    if inserisci_data(connection, giorno, mese, anno, cod_torneo):
        if inserisci_tabellino_statistiche(connection, codice_tabellino, goal_casa, goal_ospite, codice_staff):
            query = """
            INSERT INTO partita (CodicePartita, CodiceTabellino, Giorno, Mese, Anno, NomeCasa, NomeOspite, Risultato, CodiceStadio, Biglietti, PrezzoBiglietto)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (codice_partita, codice_tabellino, giorno, mese, anno, squadra_casa, squadra_trasferta, risultato, codice_stadio, biglietti, prezzo_biglietto)
            try:
                execute_query(connection, query, values)
                connection.commit()
                print(f"Partita inserita: {giorno}-{mese}-{anno}, {squadra_casa} vs {squadra_trasferta} con risultato {risultato}, Biglietti: {biglietti}, Prezzo: {prezzo_biglietto}")

                # Aggiorna il punteggio delle squadre
                if goal_casa > goal_ospite:
                    aggiorna_punteggio_squadra(connection, squadra_casa, 3)
                    aggiorna_punteggio_squadra(connection, squadra_trasferta, -3)
                elif goal_casa < goal_ospite:
                    aggiorna_punteggio_squadra(connection, squadra_casa, -3)
                    aggiorna_punteggio_squadra(connection, squadra_trasferta, 3)
                else:
                    aggiorna_punteggio_squadra(connection, squadra_casa, 1)
                    aggiorna_punteggio_squadra(connection, squadra_trasferta, 1)

                return True
            except Exception as e:
                print(f"Errore durante l'inserimento della partita: {e}")
                connection.rollback()
                return False
    else:
        return False

def get_partite(connection):
    query = "SELECT Giorno, Mese, Anno, NomeCasa, NomeOspite, Risultato FROM partita ORDER BY Anno, Mese, Giorno"
    try:
        return fetch_query(connection, query)
    except Exception as e:
        print(f"Errore durante il recupero delle partite: {e}")
        return []
