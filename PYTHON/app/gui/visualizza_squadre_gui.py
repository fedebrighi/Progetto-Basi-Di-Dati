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
        self.tree = ttk.Treeview(self.root, columns=("Nome", "AnnoFondazione", "CittaRiferimento", "TrofeiVinti", "Quota_Iscrizione", "Punteggio"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("AnnoFondazione", text="Anno Fondazione")
        self.tree.heading("CittaRiferimento", text="Città Riferimento")
        self.tree.heading("TrofeiVinti", text="Trofei Vinti")
        self.tree.heading("Quota_Iscrizione", text="Quota Iscrizione")
        self.tree.heading("Punteggio", text="Punteggio")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = ttk.Button(self.root, text="Aggiorna Squadre", command=self.refresh_squadre)
        self.refresh_button.pack(pady=10)

        self.refresh_squadre()

    def refresh_squadre(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        connection = create_connection()
        if connection and connection.is_connected():
            print("Connessione al database stabilita")
            squadre = get_squadre(connection)
            if squadre:
                print(f"Recuperate {len(squadre)} squadre")
                for squadra in squadre:
                    print(squadra)  # Debug: stampa i dati della squadra
                    self.tree.insert("", tk.END, values=squadra)
            else:
                print("Nessuna squadra trovata")
            connection.close()
        else:
            print("Connessione al database non riuscita")
