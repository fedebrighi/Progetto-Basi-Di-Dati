from app.db import fetch_query, execute_query

def verifica_giocatore(connection, codice_fiscale, nome_squadra):
    query = "SELECT COUNT(*) FROM giocatore WHERE CodiceFiscale = %s AND NomeSquadra = %s"
    result = fetch_query(connection, query, (codice_fiscale, nome_squadra))
    return result[0][0] > 0

def scambio_giocatori(connection, cf_offerto, squadra_offerta, cf_richiesto, squadra_richiesta):
    if verifica_giocatore(connection, cf_offerto, squadra_offerta) and verifica_giocatore(connection, cf_richiesto, squadra_richiesta):
        try:
            query_scambio_1 = "UPDATE giocatore SET NomeSquadra = %s WHERE CodiceFiscale = %s"
            query_scambio_2 = "UPDATE giocatore SET NomeSquadra = %s WHERE CodiceFiscale = %s"
            query_scambio_numero_1 = "UPDATE numero SET NomeSquadra = %s WHERE CodiceFiscale = %s"
            query_scambio_numero_2 = "UPDATE numero SET NomeSquadra = %s WHERE CodiceFiscale = %s"

            execute_query(connection, query_scambio_1, (squadra_richiesta, cf_offerto))
            execute_query(connection, query_scambio_2, (squadra_offerta, cf_richiesto))
            execute_query(connection, query_scambio_numero_1, (squadra_richiesta, cf_offerto))
            execute_query(connection, query_scambio_numero_2, (squadra_offerta, cf_richiesto))

            connection.commit()
            print(f"Scambio effettuato: {cf_offerto} ora in {squadra_richiesta}, {cf_richiesto} ora in {squadra_offerta}")
            return True
        except Exception as e:
            print(f"Errore durante lo scambio: {e}")
            return False
    else:
        print("Giocatori non validi per lo scambio.")
        return False
