import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.get_squadre import get_squadre

class VisualizzaSquadreGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Visualizza Squadre")
        self.create_widgets()

    def create_widgets(self):
        # Creazione della tabella per visualizzare le squadre
        self.tree = ttk.Treeview(self.root, columns=("Nome", "AnnoFondazione", "CittRiferimento", "TrofeiVinti", "Quota_Iscrizione", "Punteggio", "PosClassifica"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("AnnoFondazione", text="Anno Fondazione")
        self.tree.heading("CittRiferimento", text="Città Riferimento")
        self.tree.heading("TrofeiVinti", text="Trofei Vinti")
        self.tree.heading("Quota_Iscrizione", text="Quota Iscrizione")
        self.tree.heading("Punteggio", text="Punteggio")
        self.tree.heading("PosClassifica", text="Posizione Classifica")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Recupera e visualizza le squadre
        connection = create_connection()
        if connection and connection.is_connected():
            print("Connessione al database stabilita")
            squadre = get_squadre(connection)
            if squadre:
                print(f"Recuperate {len(squadre)} squadre")
                for squadra in squadre:
                    self.tree.insert("", tk.END, values=(squadra.nome, squadra.annofondazione, squadra.cittariferimento, squadra.trofeivinti, squadra.quotaiscrizione, squadra.punteggio, squadra.posclassifica))
            else:
                print("Nessuna squadra trovata")
            connection.close()
        else:
            print("Connessione al database non riuscita")
