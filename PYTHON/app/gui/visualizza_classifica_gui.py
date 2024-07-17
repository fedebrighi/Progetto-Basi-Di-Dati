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
        # Creazione della tabella per visualizzare la classifica
        self.tree = ttk.Treeview(self.root, columns=("Nome", "Punteggio", "PosClassifica"), show="headings")
        self.tree.heading("Nome", text="Nome Squadra")
        self.tree.heading("Punteggio", text="Punteggio")
        self.tree.heading("PosClassifica", text="Posizione Classifica")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Recupera e visualizza la classifica
        connection = create_connection()
        if connection and connection.is_connected():
            print("Connessione al database stabilita")
            classifica = get_classifica(connection)
            if classifica:
                print(f"Recuperate {len(classifica)} squadre nella classifica")
                for squadra in classifica:
                    self.tree.insert("", tk.END, values=squadra)
            else:
                print("Nessuna squadra trovata")
            connection.close()
        else:
            print("Connessione al database non riuscita")
