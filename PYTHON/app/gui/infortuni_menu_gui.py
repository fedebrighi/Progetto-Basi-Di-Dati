import tkinter as tk
from tkinter import ttk
from app.gui.registra_infortunio_gui import RegistraInfortunioGUI
from app.gui.visualizza_infortunati_gui import VisualizzaInfortunatiGUI

class InfortuniMenuGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Infortuni")
        self.create_widgets()

    def create_widgets(self):
        self.button_registra = ttk.Button(self.root, text="Registra Infortunio", command=self.open_registra_infortunio)
        self.button_registra.grid(column=0, row=0, padx=20, pady=20)

        self.button_visualizza = ttk.Button(self.root, text="Visualizza Infortunati", command=self.open_visualizza_infortunati)
        self.button_visualizza.grid(column=1, row=0, padx=20, pady=20)

    def open_registra_infortunio(self):
        RegistraInfortunioGUI(self.root)

    def open_visualizza_infortunati(self):
        VisualizzaInfortunatiGUI(self.root)
