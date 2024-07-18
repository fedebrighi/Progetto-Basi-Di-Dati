import tkinter as tk
from tkinter import ttk
from app.gui.blocca_sblocca_giocatore_gui import BloccaSbloccaGiocatoreGUI
from app.gui.visualizza_espulsi_gui import VisualizzaEspulsiGUI

class BloccaSbloccaMenuGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Blocca/Sblocca Giocatore Espulso")
        self.create_widgets()

    def create_widgets(self):
        self.button_blocca_sblocca = ttk.Button(self.root, text="Blocca/Sblocca Giocatore", command=self.open_blocca_sblocca_giocatore)
        self.button_blocca_sblocca.grid(column=0, row=0, padx=20, pady=20)

        self.button_visualizza = ttk.Button(self.root, text="Visualizza Espulsi", command=self.open_visualizza_espulsi)
        self.button_visualizza.grid(column=1, row=0, padx=20, pady=20)

    def open_blocca_sblocca_giocatore(self):
        BloccaSbloccaGiocatoreGUI(self.root)

    def open_visualizza_espulsi(self):
        VisualizzaEspulsiGUI(self.root)
