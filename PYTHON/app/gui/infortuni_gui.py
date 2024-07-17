import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.infortuni import registra_infortunio

class InfortuniGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Registrare Infortunio")
        self.create_widgets()

    def create_widgets(self):
        # Label e Entry per l'ID del giocatore
        self.label_id_giocatore = ttk.Label(self.root, text="ID Giocatore:")
        self.label_id_giocatore.grid(column=0, row=0, padx=10, pady=10)
        self.entry_id_giocatore = ttk.Entry(self.root)
        self.entry_id_giocatore.grid(column=1, row=0, padx=10, pady=10)

        # Label e Entry per la descrizione dell'infortunio
        self.label_descrizione = ttk.Label(self.root, text="Descrizione:")
        self.label_descrizione.grid(column=0, row=1, padx=10, pady=10)
        self.entry_descrizione = ttk.Entry(self.root)
        self.entry_descrizione.grid(column=1, row=1, padx=10, pady=10)

        # Label e Entry per la durata prevista dell'assenza
        self.label_durata = ttk.Label(self.root, text="Durata (giorni):")
        self.label_durata.grid(column=0, row=2, padx=10, pady=10)
        self.entry_durata = ttk.Entry(self.root)
        self.entry_durata.grid(column=1, row=2, padx=10, pady=10)

        # Bottone per inviare i dati
        self.btn_submit = ttk.Button(self.root, text="Registra Infortunio", command=self.submit)
        self.btn_submit.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    def submit(self):
        id_giocatore = int(self.entry_id_giocatore.get())
        descrizione = self.entry_descrizione.get()
        durata_giorni = int(self.entry_durata.get())

        connection = create_connection()
        registra_infortunio(connection, id_giocatore, descrizione, durata_giorni)
        connection.close()

        # Messaggio di conferma
        self.label_conferma = ttk.Label(self.root, text="Infortunio registrato con successo!")
        self.label_conferma.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
