from app.db import fetch_query

def get_totale_fondi_e_spese_torneo(connection, cod_torneo):
    query = "SELECT TotaleFondi,Spese FROM info_torneo WHERE CodTorneo = %s"
    try:
        result = fetch_query(connection, query, (cod_torneo,))
        print(f"Totale fondi e spese del torneo {cod_torneo}: {result}")
        return result[0] if result and result[0] is not None else (0, 0)
    except Exception as e:
        print(f"Errore durante il recupero del totale fondi e spese del torneo: {e}")
        return (0, 0)

def get_ricavi_sponsor(connection, cod_torneo):
    query = "SELECT SUM(Contributo) FROM sponsor_torneo WHERE CodTorneo = %s"
    try:
        result = fetch_query(connection, query, (cod_torneo,))
        print(f"Ricavi sponsor del torneo {cod_torneo}: {result}")
        return result[0][0] if result and result[0][0] is not None else 0
    except Exception as e:
        print(f"Errore durante il recupero dei ricavi degli sponsor: {e}")
        return 0

def get_contributi_televisioni(connection, cod_torneo):
    query = """
    SELECT SUM(t.Contributo) 
    FROM televisione t
    JOIN trasmissione tr ON t.Nome = tr.NomeTV
    WHERE tr.CodTorneo = %s
    """
    try:
        result = fetch_query(connection, query, (cod_torneo,))
        print(f"Contributi televisioni del torneo {cod_torneo}: {result}")
        return result[0][0] if result and result[0][0] is not None else 0
    except Exception as e:
        print(f"Errore durante il recupero dei contributi delle televisioni: {e}")
        return 0
