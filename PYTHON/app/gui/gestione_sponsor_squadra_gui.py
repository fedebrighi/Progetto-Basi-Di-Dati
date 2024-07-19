import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.get_fondi_squadra import get_fondi_squadra

class GestioneSponsorSquadraGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Gestione Sponsor Squadra")
        self.create_widgets()

    def create_widgets(self):
        self.label_presidente = ttk.Label(self.root, text="Nome Presidente:")
        self.label_presidente.pack(pady=5)
        self.entry_presidente = ttk.Entry(self.root)
        self.entry_presidente.pack(pady=5)

        self.label_cognome = ttk.Label(self.root, text="Cognome Presidente:")
        self.label_cognome.pack(pady=5)
        self.entry_cognome = ttk.Entry(self.root)
        self.entry_cognome.pack(pady=5)

        self.btn_cerca = ttk.Button(self.root, text="Cerca", command=self.visualizza_fondi)
        self.btn_cerca.pack(pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)

    def visualizza_fondi(self):
        nome_presidente = self.entry_presidente.get()
        cognome_presidente = self.entry_cognome.get()

        if nome_presidente and cognome_presidente:
            connection = create_connection()
            if connection and connection.is_connected():
                fondi_totali = get_fondi_squadra(connection, nome_presidente, cognome_presidente)
                if fondi_totali is not None:
                    self.result_label.config(text=f"Fondi Totali: {fondi_totali} €")
                else:
                    self.result_label.config(text="Presidente non trovato o nessun fondo disponibile.")
                connection.close()
            else:
                self.result_label.config(text="Connessione al database non riuscita")
        else:
            self.result_label.config(text="Inserisci sia il nome che il cognome del presidente.")
