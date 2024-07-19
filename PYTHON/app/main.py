import sys
import os

# Aggiungi il percorso del progetto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk
from app.gui.iscrizione_gui import IscrizioneGUI
from app.gui.scambi_gui import ScambiGUI
from app.gui.infortuni_menu_gui import InfortuniMenuGUI
from app.gui.visualizza_squadre_gui import VisualizzaSquadreGUI
from app.gui.visualizza_classifica_gui import VisualizzaClassificaGUI
from app.gui.elimina_squadra_gui import EliminaSquadraGUI
from app.gui.visualizza_giocatori_gui import VisualizzaGiocatoriGUI
from app.gui.inserisci_giocatore_gui import InserisciGiocatoreGUI
from app.gui.elimina_giocatore_gui import EliminaGiocatoreGUI
from app.gui.blocca_sblocca_menu_gui import BloccaSbloccaMenuGUI
from app.gui.gestione_sponsor_torneo_gui import GestioneSponsorTorneoGUI
from app.gui.visualizza_ricavi_torneo_gui import VisualizzaRicaviTorneoGUI
from app.gui.organizza_partite_gui import OrganizzaPartiteGUI

class CampionatoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campionato Manager")
        self.root.geometry("800x800")
        self.visualizza_giocatori_gui = None
        self.create_widgets()

    def create_widgets(self):
        title_font = Font(family="Helvetica", size=24, weight="bold")
        button_font = Font(family="Helvetica", size=12)

        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # Carica l'immagine
        image = Image.open("LOGO.png")
        image = image.resize((150, 150), Image.Resampling.LANCZOS)  # Ridimensiona l'immagine se necessario
        self.photo = ImageTk.PhotoImage(image)

        self.label_image = ttk.Label(main_frame, image=self.photo)
        self.label_image.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

        self.label = ttk.Label(main_frame, text="BENVENUTI NEL CHAMPION HUB", font=title_font)
        self.label.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        buttons = [
            ("Iscrizione Squadra", self.open_iscrizione),
            ("Proporre Scambio Giocatori", self.open_scambi),
            ("INFORTUNI", self.open_infortuni_menu),
            ("Visualizza Squadre", self.open_visualizza_squadre),
            ("Visualizza Classifica", self.open_visualizza_classifica),
            ("Eliminazione Squadra", self.open_eliminazione_squadra),
            ("Visualizza Giocatori", self.open_visualizza_giocatori),
            ("Inserisci Giocatori nelle Squadre", self.open_inserisci_giocatori),
            ("Elimina Giocatori", self.open_elimina_giocatori),
            ("Blocca/Sblocca Giocatore Espulso", self.open_blocca_sblocca_menu),
            ("Registrazione Dettagli Partite", self.registra_partite),
            ("Organizzazione Partite tra Squadre", self.open_organizza_partite),
            ("Gestione Sponsor Squadra", self.gestisci_sponsor_squadra),
            ("Gestione Sponsor Torneo", self.open_gestione_sponsor_torneo),
            ("Visualizza Calendario Partite", self.visualizza_calendario),
            ("Visualizza Ricavi Torneo", self.open_visualizza_ricavi_torneo),
            ("Visualizza Ricavi Presidente", self.visualizza_ricavi_presidente),
            ("Visualizza Migliori Statistiche", self.visualizza_migliori_statistiche)
        ]

        for i, (text, command) in enumerate(buttons):
            button = tk.Button(main_frame, text=text, command=command, font=button_font, width=30)
            button.grid(column=i % 2, row=i // 2 + 2, padx=10, pady=10, sticky=(tk.W, tk.E))

        for i in range(len(buttons) // 2 + 2):
            main_frame.rowconfigure(i, weight=1)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def open_iscrizione(self):
        IscrizioneGUI(self.root)

    def open_scambi(self):
        if self.visualizza_giocatori_gui is None:
            self.visualizza_giocatori_gui = VisualizzaGiocatoriGUI(self.root)
        ScambiGUI(self.root, self.visualizza_giocatori_gui)

    def open_infortuni_menu(self):
        InfortuniMenuGUI(self.root)

    def open_blocca_sblocca_menu(self):
        BloccaSbloccaMenuGUI(self.root)

    def open_visualizza_squadre(self):
        VisualizzaSquadreGUI(self.root)

    def open_visualizza_classifica(self):
        VisualizzaClassificaGUI(self.root)
    
    def open_eliminazione_squadra(self):
        EliminaSquadraGUI(self.root)
    
    def open_visualizza_giocatori(self):
        self.visualizza_giocatori_gui = VisualizzaGiocatoriGUI(self.root)

    def open_inserisci_giocatori(self):
        InserisciGiocatoreGUI(self.root)

    def open_elimina_giocatori(self):
        EliminaGiocatoreGUI(self.root)

    def open_gestione_sponsor_torneo(self):
        GestioneSponsorTorneoGUI(self.root)

    def open_visualizza_ricavi_torneo(self):
        VisualizzaRicaviTorneoGUI(self.root)

    def open_organizza_partite(self):
        OrganizzaPartiteGUI(self.root)

    def blocca_sblocca_giocatore(self):
        print("Blocca/Sblocca Giocatore Espulso")

    def registra_partite(self):
        print("Registrazione Dettagli Partite")

    def organizza_partite(self):
        print("Organizzazione Partite tra Squadre")

    def gestisci_sponsor_squadra(self):
        print("Gestione Sponsor Squadra")

    def visualizza_calendario(self):
        print("Visualizza Calendario Partite")

    def visualizza_ricavi_presidente(self):
        print("Visualizza Ricavi Presidente")

    def visualizza_migliori_statistiche(self):
        print("Visualizza Migliori Statistiche")

if __name__ == "__main__":
    root = tk.Tk()
    app = CampionatoApp(root)
    root.mainloop()
