import sys
import os

# Aggiungi il percorso del progetto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from app.gui.iscrizione_gui import IscrizioneGUI
from app.gui.scambi_gui import ScambiGUI
from app.gui.infortuni_gui import InfortuniGUI
from app.gui.visualizza_squadre_gui import VisualizzaSquadreGUI
from app.gui.visualizza_classifica_gui import VisualizzaClassificaGUI
from app.gui.elimina_squadra_gui import EliminaSquadraGUI
from app.gui.visualizza_giocatori_gui import VisualizzaGiocatoriGUI

class CampionatoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campionato Manager")
        self.root.geometry("600x600")
        self.visualizza_giocatori_gui = None
        self.create_widgets()

    def create_widgets(self):
        title_font = Font(family="Helvetica", size=24, weight="bold")
        button_font = Font(family="Helvetica", size=10)

        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        self.label = ttk.Label(main_frame, text="BENVENUTI NEL CHAMPION HUB", font=title_font)
        self.label.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

        buttons = [
            ("Iscrizione Squadra", self.open_iscrizione),
            ("Proporre Scambio Giocatori", self.open_scambi),
            ("Registrare Infortunio", self.open_infortuni),
            ("Visualizza Squadre", self.open_visualizza_squadre),
            ("Visualizza Classifica", self.open_visualizza_classifica),
            ("Eliminazione Squadra", self.open_eliminazione_squadra),
            ("Visualizza Giocatori", self.open_visualizza_giocatori),
            ("Inserisci Giocatori nelle Squadre", self.inserisci_giocatori),
            ("Blocca/Sblocca Giocatore Espulso", self.blocca_sblocca_giocatore),
            ("Registrazione Dettagli Partite", self.registra_partite),
            ("Organizzazione Partite tra Squadre", self.organizza_partite),
            ("Gestione Sponsor Squadra", self.gestisci_sponsor_squadra),
            ("Gestione Sponsor Torneo", self.gestisci_sponsor_torneo),
            ("Visualizza Calendario Partite", self.visualizza_calendario),
            ("Visualizza Ricavi Torneo", self.visualizza_ricavi_torneo),
            ("Visualizza Ricavi Presidente", self.visualizza_ricavi_presidente),
            ("Visualizza Migliori Statistiche", self.visualizza_migliori_statistiche)
        ]

        for i, (text, command) in enumerate(buttons):
            button = tk.Button(main_frame, text=text, command=command, font=button_font)
            button.grid(column=i % 2, row=i // 2 + 1, padx=10, pady=10, sticky=(tk.W, tk.E))

        for i in range(len(buttons) // 2 + 1):
            main_frame.rowconfigure(i, weight=1)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def open_iscrizione(self):
        IscrizioneGUI(self.root)

    def open_scambi(self):
        if self.visualizza_giocatori_gui is None:
            self.visualizza_giocatori_gui = VisualizzaGiocatoriGUI(self.root)
        ScambiGUI(self.root, self.visualizza_giocatori_gui)

    def open_infortuni(self):
        InfortuniGUI(self.root)

    def open_visualizza_squadre(self):
        VisualizzaSquadreGUI(self.root)

    def open_visualizza_classifica(self):
        VisualizzaClassificaGUI(self.root)
    
    def open_eliminazione_squadra(self):
        EliminaSquadraGUI(self.root)
    
    def open_visualizza_giocatori(self):
        self.visualizza_giocatori_gui = VisualizzaGiocatoriGUI(self.root)

    # Placeholder methods for new buttons
    def inserisci_giocatori(self):
        print("Inserisci Giocatori nelle Squadre")

    def blocca_sblocca_giocatore(self):
        print("Blocca/Sblocca Giocatore Espulso")

    def registra_partite(self):
        print("Registrazione Dettagli Partite")

    def organizza_partite(self):
        print("Organizzazione Partite tra Squadre")

    def gestisci_sponsor_squadra(self):
        print("Gestione Sponsor Squadra")

    def gestisci_sponsor_torneo(self):
        print("Gestione Sponsor Torneo")

    def visualizza_calendario(self):
        print("Visualizza Calendario Partite")

    def visualizza_ricavi_torneo(self):
        print("Visualizza Ricavi Torneo")

    def visualizza_ricavi_presidente(self):
        print("Visualizza Ricavi Presidente")

    def visualizza_migliori_statistiche(self):
        print("Visualizza Migliori Statistiche")

if __name__ == "__main__":
    root = tk.Tk()
    app = CampionatoApp(root)
    root.mainloop()
