import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.gestione_sponsor_torneo import get_sponsor_torneo, get_totale_ricavi_sponsor
from app.gui.aggiungi_sponsor_gui import AggiungiSponsorGUI

class GestioneSponsorTorneoGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Gestione Sponsor Torneo")
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("Nome", "Contributo"), show="headings")
        self.tree.heading("Nome", text="Nome Sponsor")
        self.tree.heading("Contributo", text="Contributo")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.label_totale = ttk.Label(self.root, text="Totale Ricavi: ")
        self.label_totale.pack(pady=10)

        self.button_aggiungi = ttk.Button(self.root, text="Aggiungi Sponsor", command=self.open_aggiungi_sponsor)
        self.button_aggiungi.pack(pady=5)

        self.button_aggiorna = ttk.Button(self.root, text="Aggiorna Visualizzazione", command=self.refresh_sponsor)
        self.button_aggiorna.pack(pady=5)

        self.refresh_sponsor()

    def refresh_sponsor(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        connection = create_connection()
        if connection and connection.is_connected():
            sponsor = get_sponsor_torneo(connection)
            totale_ricavi = get_totale_ricavi_sponsor(connection)
            connection.close()

            for s in sponsor:
                self.tree.insert("", tk.END, values=s)

            self.label_totale.config(text=f"Totale Ricavi: {totale_ricavi} €")

    def open_aggiungi_sponsor(self):
        AggiungiSponsorGUI(self.root, self.refresh_sponsor)
