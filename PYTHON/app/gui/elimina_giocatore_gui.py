import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.elimina_giocatore import elimina_giocatore

class EliminaGiocatoreGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Elimina Giocatore")
        self.create_widgets()

    def create_widgets(self):
        self.label_codice_fiscale = ttk.Label(self.root, text="Codice Fiscale:")
        self.label_codice_fiscale.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
        self.entry_codice_fiscale = ttk.Entry(self.root, width=30)
        self.entry_codice_fiscale.grid(column=1, row=0, padx=10, pady=5)

        self.button_elimina = ttk.Button(self.root, text="Elimina", command=self.elimina_giocatore)
        self.button_elimina.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    def elimina_giocatore(self):
        codice_fiscale = self.entry_codice_fiscale.get()

        if codice_fiscale:
            connection = create_connection()
            if connection and connection.is_connected():
                successo = elimina_giocatore(connection, codice_fiscale)
                connection.close()
                if successo:
                    self.result_label.config(text="Giocatore eliminato con successo!", foreground="green")
                else:
                    self.result_label.config(text="Errore durante l'eliminazione del giocatore.", foreground="red")
            else:
                self.result_label.config(text="Connessione al database non riuscita.", foreground="red")
        else:
            self.result_label.config(text="Il campo Codice Fiscale è obbligatorio.", foreground="red")
