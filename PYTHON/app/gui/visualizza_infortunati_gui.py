import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.visualizza_infortunati import get_giocatori_infortunati

class VisualizzaInfortunatiGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Giocatori Infortunati")
        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("Nome", "NomeSquadra", "Infortunio"), show="headings")
        self.tree.heading("Nome", text="Nome Giocatore")
        self.tree.heading("NomeSquadra", text="Nome Squadra")
        self.tree.heading("Infortunio", text="Stato Infortunio")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_infortunati()

    def refresh_infortunati(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        connection = create_connection()
        if connection and connection.is_connected():
            giocatori_infortunati = get_giocatori_infortunati(connection)
            connection.close()
            for giocatore in giocatori_infortunati:
                self.tree.insert("", tk.END, values=giocatore)
