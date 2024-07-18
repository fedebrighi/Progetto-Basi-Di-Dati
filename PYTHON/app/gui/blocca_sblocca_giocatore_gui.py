import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.blocca_sblocca_giocatore import blocca_sblocca_giocatore

class BloccaSbloccaGiocatoreGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Blocca/Sblocca Giocatore Espulso")
        self.create_widgets()

    def create_widgets(self):
        self.label_codice_fiscale = ttk.Label(self.root, text="Codice Fiscale:")
        self.label_codice_fiscale.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
        self.entry_codice_fiscale = ttk.Entry(self.root, width=30)
        self.entry_codice_fiscale.grid(column=1, row=0, padx=10, pady=5)

        self.label_stato_espulsione = ttk.Label(self.root, text="Stato Espulsione:")
        self.label_stato_espulsione.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
        self.entry_stato_espulsione = ttk.Entry(self.root, width=30)
        self.entry_stato_espulsione.grid(column=1, row=1, padx=10, pady=5)

        self.button_aggiorna = ttk.Button(self.root, text="Aggiorna", command=self.aggiorna_espulsione)
        self.button_aggiorna.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    def aggiorna_espulsione(self):
        codice_fiscale = self.entry_codice_fiscale.get()
        stato_espulsione = self.entry_stato_espulsione.get()

        if codice_fiscale and stato_espulsione:
            connection = create_connection()
            if connection and connection.is_connected():
                successo = blocca_sblocca_giocatore(connection, codice_fiscale, stato_espulsione)
                connection.close()
                if successo:
                    self.result_label.config(text="Stato di espulsione aggiornato con successo!", foreground="green")
                else:
                    self.result_label.config(text="Errore durante l'aggiornamento dello stato di espulsione.", foreground="red")
            else:
                self.result_label.config(text="Connessione al database non riuscita.", foreground="red")
        else:
            self.result_label.config(text="Tutti i campi sono obbligatori.", foreground="red")
