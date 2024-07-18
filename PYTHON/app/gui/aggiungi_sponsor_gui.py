import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.gestione_sponsor_torneo import aggiungi_sponsor_torneo

class AggiungiSponsorGUI:
    def __init__(self, root, refresh_callback):
        self.root = tk.Toplevel(root)
        self.root.title("Aggiungi Sponsor")
        self.refresh_callback = refresh_callback
        self.create_widgets()

    def create_widgets(self):
        self.label_nome = ttk.Label(self.root, text="Nome Sponsor:")
        self.label_nome.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
        self.entry_nome = ttk.Entry(self.root, width=30)
        self.entry_nome.grid(column=1, row=0, padx=10, pady=5)

        self.label_contributo = ttk.Label(self.root, text="Contributo:")
        self.label_contributo.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
        self.entry_contributo = ttk.Entry(self.root, width=30)
        self.entry_contributo.grid(column=1, row=1, padx=10, pady=5)

        # Aggiungere un campo per CodTorneo
        self.label_cod_torneo = ttk.Label(self.root, text="Codice Torneo:")
        self.label_cod_torneo.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
        self.entry_cod_torneo = ttk.Entry(self.root, width=30)
        self.entry_cod_torneo.grid(column=1, row=2, padx=10, pady=5)

        self.button_aggiungi = ttk.Button(self.root, text="Aggiungi", command=self.aggiungi_sponsor)
        self.button_aggiungi.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

    def aggiungi_sponsor(self):
        nome = self.entry_nome.get()
        contributo = self.entry_contributo.get()
        cod_torneo = self.entry_cod_torneo.get()

        if nome and contributo and cod_torneo:
            connection = create_connection()
            if connection and connection.is_connected():
                successo = aggiungi_sponsor_torneo(connection, nome, contributo, cod_torneo)
                connection.close()
                if successo:
                    self.result_label.config(text="Sponsor aggiunto con successo!", foreground="green")
                    self.refresh_callback()
                    self.root.destroy()  # Chiude la finestra dopo aver aggiunto lo sponsor
                else:
                    self.result_label.config(text="Errore durante l'aggiunta dello sponsor.", foreground="red")
            else:
                self.result_label.config(text="Connessione al database non riuscita.", foreground="red")
        else:
            self.result_label.config(text="Tutti i campi sono obbligatori.", foreground="red")
