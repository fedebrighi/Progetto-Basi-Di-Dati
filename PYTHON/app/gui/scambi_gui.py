import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.scambi import proponi_scambio, esegui_scambio

class ScambiGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Proporre Scambio Giocatori")
        self.create_widgets()

    def create_widgets(self):
        # Label e Entry per l'ID del giocatore offerto
        self.label_id_giocatore_offerto = ttk.Label(self.root, text="ID Giocatore Offerto:")
        self.label_id_giocatore_offerto.grid(column=0, row=0, padx=10, pady=10)
        self.entry_id_giocatore_offerto = ttk.Entry(self.root)
        self.entry_id_giocatore_offerto.grid(column=1, row=0, padx=10, pady=10)

        # Label e Entry per l'ID della squadra destinataria
        self.label_id_squadra_destinazione = ttk.Label(self.root, text="ID Squadra Destinazione:")
        self.label_id_squadra_destinazione.grid(column=0, row=1, padx=10, pady=10)
        self.entry_id_squadra_destinazione = ttk.Entry(self.root)
        self.entry_id_squadra_destinazione.grid(column=1, row=1, padx=10, pady=10)

        # Label e Entry per l'ID del giocatore richiesto
        self.label_id_giocatore_richiesto = ttk.Label(self.root, text="ID Giocatore Richiesto:")
        self.label_id_giocatore_richiesto.grid(column=0, row=2, padx=10, pady=10)
        self.entry_id_giocatore_richiesto = ttk.Entry(self.root)
        self.entry_id_giocatore_richiesto.grid(column=1, row=2, padx=10, pady=10)

        # Label e Entry per l'ID della squadra proponente
        self.label_id_squadra_proponente = ttk.Label(self.root, text="ID Squadra Proponente:")
        self.label_id_squadra_proponente.grid(column=0, row=3, padx=10, pady=10)
        self.entry_id_squadra_proponente = ttk.Entry(self.root)
        self.entry_id_squadra_proponente.grid(column=1, row=3, padx=10, pady=10)

        # Bottone per proporre lo scambio
        self.btn_proponi_scambio = ttk.Button(self.root, text="Proponi Scambio", command=self.proponi_scambio)
        self.btn_proponi_scambio.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

        # Bottone per eseguire lo scambio
        self.btn_esegui_scambio = ttk.Button(self.root, text="Esegui Scambio", command=self.esegui_scambio)
        self.btn_esegui_scambio.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

    def proponi_scambio(self):
        id_giocatore_offerto = int(self.entry_id_giocatore_offerto.get())
        id_squadra_destinazione = int(self.entry_id_squadra_destinazione.get())
        id_giocatore_richiesto = int(self.entry_id_giocatore_richiesto.get())
        id_squadra_proponente = int(self.entry_id_squadra_proponente.get())

        connection = create_connection()
        proponi_scambio(connection, id_giocatore_offerto, id_squadra_destinazione, id_giocatore_richiesto, id_squadra_proponente)
        connection.close()

        # Messaggio di conferma
        self.label_conferma = ttk.Label(self.root, text="Scambio proposto con successo!")
        self.label_conferma.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

    def esegui_scambio(self):
        id_giocatore_offerto = int(self.entry_id_giocatore_offerto.get())
        id_squadra_destinazione = int(self.entry_id_squadra_destinazione.get())
        id_giocatore_richiesto = int(self.entry_id_giocatore_richiesto.get())
        id_squadra_proponente = int(self.entry_id_squadra_proponente.get())

        connection = create_connection()
        esegui_scambio(connection, id_giocatore_offerto, id_squadra_destinazione, id_giocatore_richiesto, id_squadra_proponente)
        connection.close()

        # Messaggio di conferma
        self.label_conferma = ttk.Label(self.root, text="Scambio eseguito con successo!")
        self.label_conferma.grid(column=0, row=6, columnspan=2, padx=10, pady=10)
