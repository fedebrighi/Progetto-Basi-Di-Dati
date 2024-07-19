from app.db import fetch_query

def get_fondi_squadra(connection, nome_presidente, cognome_presidente):
    query = """
    SELECT SUM(f.Totale + s.Quota) as FondiTotali
    FROM presidente p
    JOIN fondi f ON p.CodiceFiscale = f.CodicePresidente
    JOIN contribuzione c ON f.IBAN = c.IBAN
    JOIN sponsor s ON c.NomeSponsor = s.Nome
    WHERE p.Nome = %s AND p.Cognome = %s
    """
    values = (nome_presidente, cognome_presidente)
    result = fetch_query(connection, query, values)
    if result:
        return result[0][0]
    return None
