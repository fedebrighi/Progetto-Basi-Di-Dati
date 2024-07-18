import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.visualizza_ricavi_torneo import get_totale_fondi_e_spese_torneo, get_ricavi_sponsor, get_contributi_televisioni

class VisualizzaRicaviTorneoGUI:
    def __init__(self, root, cod_torneo):
        self.root = tk.Toplevel(root)
        self.root.title("Visualizza Ricavi Torneo")
        self.cod_torneo = cod_torneo
        self.create_widgets()
        self.refresh_ricavi()

    def create_widgets(self):
        self.label_totale_fondi = ttk.Label(self.root, text="Totale Fondi Torneo: ")
        self.label_totale_fondi.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
        
        self.label_spese = ttk.Label(self.root, text="Spese del Torneo: ")
        self.label_spese.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
        
        self.label_ricavi_sponsor = ttk.Label(self.root, text="Ricavi dagli Sponsor: ")
        self.label_ricavi_sponsor.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
        
        self.label_contributi_televisioni = ttk.Label(self.root, text="Contributi delle Televisioni: ")
        self.label_contributi_televisioni.grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)

        self.label_totale_finale = ttk.Label(self.root, text="Ricavi Torneo: ", foreground="green")
        self.label_totale_finale.grid(column=0, row=4, padx=10, pady=10, sticky=tk.W)

    def refresh_ricavi(self):
        connection = create_connection()
        if connection and connection.is_connected():
            totale_fondi, spese = get_totale_fondi_e_spese_torneo(connection, self.cod_torneo)
            ricavi_sponsor = get_ricavi_sponsor(connection, self.cod_torneo)
            contributi_televisioni = get_contributi_televisioni(connection, self.cod_torneo)
            totale_finale = totale_fondi - spese + ricavi_sponsor + contributi_televisioni

            print(f"Totale fondi: {totale_fondi}, Spese: {spese}, Ricavi sponsor: {ricavi_sponsor}, Contributi televisioni: {contributi_televisioni}")

            self.label_totale_fondi.config(text=f"Totale Fondi Torneo: {totale_fondi} €")
            self.label_spese.config(text=f"Spese del Torneo: {spese} €")
            self.label_ricavi_sponsor.config(text=f"Ricavi dagli Sponsor: {ricavi_sponsor} €")
            self.label_contributi_televisioni.config(text=f"Contributi delle Televisioni: {contributi_televisioni} €")
            self.label_totale_finale.config(text=f"Ricavi Torneo: {totale_finale} €")

            connection.close()
        else:
            tk.messagebox.showerror("Errore", "Connessione al database non riuscita.")
