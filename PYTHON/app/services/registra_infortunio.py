import tkinter as tk
from tkinter import ttk
from app.gui.visualizza_infortunati_gui import VisualizzaInfortunatiGUI

from app.db import execute_query

def registra_infortunio(connection, codice_fiscale, stato_infortunio):
    query = "UPDATE giocatore SET Infortunio = %s WHERE CodiceFiscale = %s"
    values = (stato_infortunio, codice_fiscale)

    try:
        execute_query(connection, query, values)
        connection.commit()
        return True
    except Exception as e:
        print(f"Errore durante la registrazione dell'infortunio: {e}")
        connection.rollback()
        return False
