from app.db import fetch_query

def get_fondi_squadra(connection, nome_presidente, cognome_presidente):
    query = """
    SELECT SUM(f.Totale + s.Quota - COALESCE(g.Stipendio, 0) - COALESCE(a.Stipendio, 0) - COALESCE(ds.Stipendio, 0)) as FondiTotali
    FROM presidente p
    JOIN fondi f ON p.CodiceFiscale = f.CodicePresidente
    JOIN direttore_sportivo ds ON f.CodiceDir = ds.CodiceFiscale
    JOIN allenatore a ON ds.CodiceFiscale = a.Sce_CodiceFiscale
    JOIN squadra sq ON a.All_Nome = sq.Nome
    LEFT JOIN giocatore g ON sq.Nome = g.NomeSquadra
    JOIN contribuzione c ON f.IBAN = c.IBAN
    JOIN sponsor s ON c.NomeSponsor = s.Nome
    WHERE p.Nome = %s AND p.Cognome = %s
    """
    values = (nome_presidente, cognome_presidente)
    result = fetch_query(connection, query, values)
    if result:
        return result[0][0]
    return None
