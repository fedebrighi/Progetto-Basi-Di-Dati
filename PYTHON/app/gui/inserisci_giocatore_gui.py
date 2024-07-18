import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.inserisci_giocatore import inserisci_giocatore

class InserisciGiocatoreGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Inserisci Giocatore")
        self.create_widgets()

    def create_widgets(self):
        fields = [
            "Codice Fiscale", "Nome", "Cognome", "Data di Nascita (YYYY-MM-DD)", "Nazionalità", 
            "Stipendio", "Infortunio", "Espulsione", "Nome Squadra", "Numero di Maglia", "Ruolo"
        ]
        self.entries = {}
        
        for i, field in enumerate(fields):
            label = ttk.Label(self.root, text=field)
            label.grid(column=0, row=i, padx=10, pady=5, sticky=tk.W)
            entry = ttk.Entry(self.root, width=30)
            entry.grid(column=1, row=i, padx=10, pady=5)
            self.entries[field] = entry

        self.button_inserisci = ttk.Button(self.root, text="Inserisci", command=self.inserisci_giocatore)
        self.button_inserisci.grid(column=0, row=len(fields), columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=len(fields) + 1, columnspan=2, padx=10, pady=10)

    def inserisci_giocatore(self):
        values = [entry.get() for entry in self.entries.values()]

        if all(values):
            connection = create_connection()
            if connection and connection.is_connected():
                successo = inserisci_giocatore(connection, *values)
                connection.close()
                if successo:
                    self.result_label.config(text="Giocatore inserito con successo!", foreground="green")
                else:
                    self.result_label.config(text="Errore durante l'inserimento del giocatore.", foreground="red")
            else:
                self.result_label.config(text="Connessione al database non riuscita.", foreground="red")
        else:
            self.result_label.config(text="Tutti i campi sono obbligatori.", foreground="red")
