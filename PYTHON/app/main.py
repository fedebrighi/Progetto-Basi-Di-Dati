import tkinter as tk
from tkinter import ttk
from app.gui.iscrizione_gui import IscrizioneGUI
from app.gui.scambi_gui import ScambiGUI
from app.gui.infortuni_gui import InfortuniGUI
from app.gui.visualizza_squadre_gui import VisualizzaSquadreGUI
from app.gui.visualizza_classifica_gui import VisualizzaClassificaGUI

class CampionatoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campionato Manager")
        
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Benvenuto nel Campionato Manager")
        self.label.grid(column=0, row=0, padx=10, pady=10)
        
        self.btn_iscrizione = ttk.Button(self.root, text="Iscrizione Squadra", command=self.open_iscrizione)
        self.btn_iscrizione.grid(column=0, row=1, padx=10, pady=10)
        
        self.btn_scambio = ttk.Button(self.root, text="Proporre Scambio Giocatori", command=self.open_scambi)
        self.btn_scambio.grid(column=0, row=2, padx=10, pady=10)
        
        self.btn_infortunio = ttk.Button(self.root, text="Registrare Infortunio", command=self.open_infortuni)
        self.btn_infortunio.grid(column=0, row=3, padx=10, pady=10)

        self.btn_visualizza_squadre = ttk.Button(self.root, text="Visualizza Squadre", command=self.open_visualizza_squadre)
        self.btn_visualizza_squadre.grid(column=0, row=4, padx=10, pady=10)

        self.btn_visualizza_classifica = ttk.Button(self.root, text="Visualizza Classifica", command=self.open_visualizza_classifica)
        self.btn_visualizza_classifica.grid(column=0, row=5, padx=10, pady=10)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = CampionatoApp(root)
    root.mainloop()
