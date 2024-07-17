import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.get_classifica import get_classifica

import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.get_classifica import get_classifica

class VisualizzaClassificaGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Visualizza Classifica")
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("Nome", "Punteggio", "PosClassifica"), show="headings")
        self.tree.heading("Nome", text="Nome Squadra")
        self.tree.heading("Punteggio", text="Punteggio")
        self.tree.heading("PosClassifica", text="Posizione Classifica")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = ttk.Button(self.root, text="Aggiorna Classifica", command=self.refresh_classifica)
        self.refresh_button.pack(pady=10)

        self.refresh_classifica()

    def refresh_classifica(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        connection = create_connection()
        if connection and connection.is_connected():
            print("Connessione al database stabilita")
            classifica = get_classifica(connection)
            if classifica:
                print(f"Recuperate {len(classifica)} squadre nella classifica")
                for squadra in classifica:
                    print(squadra)  # Debug: stampa i dati della squadra
                    self.tree.insert("", tk.END, values=squadra)
            else:
                print("Nessuna squadra trovata")
            connection.close()
        else:
            print("Connessione al database non riuscita")
