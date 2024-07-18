import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.registra_infortunio import registra_infortunio

class RegistraInfortunioGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Registra Infortunio")
        self.create_widgets()

    def create_widgets(self):
        self.label_codice_fiscale = ttk.Label(self.root, text="Codice Fiscale:")
        self.label_codice_fiscale.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
        self.entry_codice_fiscale = ttk.Entry(self.root, width=30)
        self.entry_codice_fiscale.grid(column=1, row=0, padx=10, pady=5)

        self.label_stato_infortunio = ttk.Label(self.root, text="Stato Infortunio:")
        self.label_stato_infortunio.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
        self.entry_stato_infortunio = ttk.Entry(self.root, width=30)
        self.entry_stato_infortunio.grid(column=1, row=1, padx=10, pady=5)

        self.button_registra = ttk.Button(self.root, text="Registra", command=self.registra_infortunio)
        self.button_registra.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    def registra_infortunio(self):
        codice_fiscale = self.entry_codice_fiscale.get()
        stato_infortunio = self.entry_stato_infortunio.get()

        if codice_fiscale and stato_infortunio:
            connection = create_connection()
            if connection and connection.is_connected():
                successo = registra_infortunio(connection, codice_fiscale, stato_infortunio)
                connection.close()
                if successo:
                    self.result_label.config(text="Infortunio registrato con successo!", foreground="green")
                else:
                    self.result_label.config(text="Errore durante la registrazione dell'infortunio.", foreground="red")
            else:
                self.result_label.config(text="Connessione al database non riuscita.", foreground="red")
        else:
            self.result_label.config(text="Tutti i campi sono obbligatori.", foreground="red")
