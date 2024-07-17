import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.iscrizione import iscrizione_squadra

class IscrizioneGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Iscrizione Squadra")
        self.create_widgets()

    def create_widgets(self):
        # Label e Entry per il nome della squadra
        self.label_nome = ttk.Label(self.root, text="Nome Squadra:")
        self.label_nome.grid(column=0, row=0, padx=10, pady=10)
        self.entry_nome = ttk.Entry(self.root)
        self.entry_nome.grid(column=1, row=0, padx=10, pady=10)

        # Label e Entry per l'anno di fondazione
        self.label_anno = ttk.Label(self.root, text="Anno Fondazione:")
        self.label_anno.grid(column=0, row=1, padx=10, pady=10)
        self.entry_anno = ttk.Entry(self.root)
        self.entry_anno.grid(column=1, row=1, padx=10, pady=10)

        # Label e Entry per la città di riferimento
        self.label_citta = ttk.Label(self.root, text="Città Riferimento:")
        self.label_citta.grid(column=0, row=2, padx=10, pady=10)
        self.entry_citta = ttk.Entry(self.root)
        self.entry_citta.grid(column=1, row=2, padx=10, pady=10)

        # Label e Entry per la quota di iscrizione
        self.label_quota = ttk.Label(self.root, text="Quota Iscrizione:")
        self.label_quota.grid(column=0, row=3, padx=10, pady=10)
        self.entry_quota = ttk.Entry(self.root)
        self.entry_quota.grid(column=1, row=3, padx=10, pady=10)

        # Label e Entry per il punteggio iniziale
        self.label_punteggio = ttk.Label(self.root, text="Punteggio Iniziale:")
        self.label_punteggio.grid(column=0, row=4, padx=10, pady=10)
        self.entry_punteggio = ttk.Entry(self.root)
        self.entry_punteggio.grid(column=1, row=4, padx=10, pady=10)

        # Label e Entry per i trofei vinti
        self.label_trofei = ttk.Label(self.root, text="Trofei Vinti:")
        self.label_trofei.grid(column=0, row=5, padx=10, pady=10)
        self.entry_trofei = ttk.Entry(self.root)
        self.entry_trofei.grid(column=1, row=5, padx=10, pady=10)

        # Bottone per iscrivere la squadra
        self.btn_submit = ttk.Button(self.root, text="Iscrivi", command=self.submit)
        self.btn_submit.grid(column=0, row=6, columnspan=2, padx=10, pady=10)

    def submit(self):
        nome_squadra = self.entry_nome.get()
        anno_squadra = int(self.entry_anno.get())
        citta_squadra = self.entry_citta.get()
        quota_squadra = int(self.entry_quota.get())
        punteggio_squadra = int(self.entry_punteggio.get())
        trofei_vinti = int(self.entry_trofei.get())

        connection = create_connection()
        iscrizione_squadra(connection, nome_squadra, anno_squadra, citta_squadra, quota_squadra, punteggio_squadra, trofei_vinti)
        connection.close()

        # Messaggio di conferma
        self.label_conferma = ttk.Label(self.root, text="Squadra iscritta con successo!")
        self.label_conferma.grid(column=0, row=7, columnspan=2, padx=10, pady=10)
