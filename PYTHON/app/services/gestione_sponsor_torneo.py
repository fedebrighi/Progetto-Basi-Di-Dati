from app.db import fetch_query, execute_query

def get_sponsor_torneo(connection):
    query = "SELECT nome, contributo FROM sponsor_torneo"
    try:
        return fetch_query(connection, query)
    except Exception as e:
        print(f"Errore durante il recupero degli sponsor del torneo: {e}")
        return []

def get_totale_ricavi_sponsor(connection):
    query = "SELECT SUM(contributo) FROM sponsor_torneo"
    try:
        result = fetch_query(connection, query)
        return result[0][0] if result and result[0][0] is not None else 0
    except Exception as e:
        print(f"Errore durante il calcolo del totale dei ricavi degli sponsor: {e}")
        return 0

def aggiungi_sponsor_torneo(connection, nome, contributo, cod_torneo):
    query = "INSERT INTO sponsor_torneo (nome, contributo, CodTorneo) VALUES (%s, %s, %s)"
    values = (nome, contributo, cod_torneo)
    try:
        execute_query(connection, query, values)
        connection.commit()
        print(f"Sponsor aggiunto: {nome}, {contributo}, {cod_torneo}")
        return True
    except Exception as e:
        print(f"Errore durante l'aggiunta di un nuovo sponsor: {e}")
        connection.rollback()
        return False
