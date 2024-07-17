import sys
import os

# Aggiungi il percorso del progetto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk
from app.gui.iscrizione_gui import IscrizioneGUI
from app.gui.scambi_gui import ScambiGUI
from app.gui.infortuni_gui import InfortuniGUI
from app.gui.visualizza_squadre_gui import VisualizzaSquadreGUI
from app.gui.visualizza_classifica_gui import VisualizzaClassificaGUI
from app.gui.elimina_squadra_gui import EliminaSquadraGUI

class CampionatoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campionato Manager")
        self.root.geometry("400x400")
        
        self.create_widgets()

    def create_widgets(self):
        # Frame principale
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurazione delle colonne e righe del frame principale
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)

        # Titolo
        self.label = ttk.Label(main_frame, text="Benvenuto nel Campionato Manager", font=("Helvetica", 16))
        self.label.grid(column=0, row=0, padx=10, pady=10)

        # Bottoni
        self.btn_iscrizione = ttk.Button(main_frame, text="Iscrizione Squadra", command=self.open_iscrizione)
        self.btn_iscrizione.grid(column=0, row=1, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_scambio = ttk.Button(main_frame, text="Proporre Scambio Giocatori", command=self.open_scambi)
        self.btn_scambio.grid(column=0, row=2, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_infortunio = ttk.Button(main_frame, text="Registrare Infortunio", command=self.open_infortuni)
        self.btn_infortunio.grid(column=0, row=3, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_visualizza_squadre = ttk.Button(main_frame, text="Visualizza Squadre", command=self.open_visualizza_squadre)
        self.btn_visualizza_squadre.grid(column=0, row=4, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_visualizza_classifica = ttk.Button(main_frame, text="Visualizza Classifica", command=self.open_visualizza_classifica)
        self.btn_visualizza_classifica.grid(column=0, row=5, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_eliminazione_squadra = ttk.Button(main_frame, text="Eliminazione Squadra", command=self.open_eliminazione_squadra)
        self.btn_eliminazione_squadra.grid(column=0, row=6, padx=10, pady=10, sticky=(tk.W, tk.E))

    def open_iscrizione(self):
        IscrizioneGUI(self.root)

    def open_scambi(self):
        ScambiGUI(self.root)

    def open_infortuni(self):
        InfortuniGUI(self.root)

    def open_visualizza_squadre(self):
        VisualizzaSquadreGUI(self.root)

    def open_visualizza_classifica(self):
        VisualizzaClassificaGUI(self.root)
    
    def open_eliminazione_squadra(self):
        EliminaSquadraGUI(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = CampionatoApp(root)
    root.mainloop()
