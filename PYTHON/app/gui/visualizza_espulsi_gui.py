import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.visualizza_espulsi import get_giocatori_espulsi

class VisualizzaEspulsiGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Giocatori Espulsi")
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("Nome","Cognome","NomeSquadra", "Espulsione"), show="headings")
        self.tree.heading("Nome", text="Nome Giocatore")
        self.tree.heading("Cognome", text="Cognome Giocatore")
        self.tree.heading("NomeSquadra", text="Nome Squadra")
        self.tree.heading("Espulsione", text="Stato Espulsione")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_espulsi()

    def refresh_espulsi(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        connection = create_connection()
        if connection and connection.is_connected():
            giocatori_espulsi = get_giocatori_espulsi(connection)
            connection.close()
            for giocatore in giocatori_espulsi:
                self.tree.insert("", tk.END, values=giocatore)
