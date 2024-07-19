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
from app.gui.organizza_partite_gui import OrganizzaPartiteGUI
from app.gui.visualizza_calendario_gui import VisualizzaCalendarioGUI
from app.gui.gestione_sponsor_squadra_gui import GestioneSponsorSquadraGUI

class CampionatoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campionato Manager")
        self.root.geometry("900x700")
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        try:
            image = Image.open("LOGO.png")
            image = image.resize((150, 150), Image.LANCZOS)
            self.logo = ImageTk.PhotoImage(image)
            self.logo_label = ttk.Label(main_frame, image=self.logo)
            self.logo_label.grid(column=0, row=0, columnspan=2, pady=10)
        except Exception as e:
            print(f"Errore durante il caricamento dell'immagine: {e}")
            self.logo_label = ttk.Label(main_frame, text="Champion Hub", font=("Helvetica", 24, "bold"))
            self.logo_label.grid(column=0, row=0, columnspan=2, pady=10)

        self.label = ttk.Label(main_frame, text="BENVENUTI NEL CHAMPION HUB", font=("Helvetica", 24, "bold"))
        self.label.grid(column=0, row=1, columnspan=2, pady=10)

        button_texts = [
            ("Iscrizione Squadra", self.open_iscrizione),
            ("Proporre Scambio Giocatori", self.open_scambi),
            ("Infortuni", self.open_infortuni),
            ("Visualizza Squadre", self.open_visualizza_squadre),
            ("Visualizza Classifica", self.open_visualizza_classifica),
            ("Eliminazione Squadra", self.open_eliminazione_squadra),
            ("Visualizza Giocatori", self.open_visualizza_giocatori),
            ("Inserisci Giocatori nelle Squadre", self.open_inserisci_giocatore),
            ("Blocca/Sblocca Giocatore Espulso", self.open_blocca_giocatore_espulso),
            ("Registrazione Dettagli Partite", self.open_organizza_partite),
            ("Gestione Sponsor Squadra", self.open_gestione_sponsor_squadra),
            ("Gestione Sponsor Torneo", self.open_gestione_sponsor_torneo),
            ("Visualizza Calendario Partite", self.open_visualizza_calendario)
        ]

        row = 2
        for i, (text, command) in enumerate(button_texts):
            col = i % 2
            btn = ttk.Button(main_frame, text=text, command=command)
            btn.grid(column=col, row=row, padx=10, pady=10, sticky=(tk.W, tk.E))
            main_frame.grid_columnconfigure(col, weight=1)
            if col == 1:
                row += 1

    def open_iscrizione(self):
        IscrizioneGUI(self.root)

    def open_scambi(self):
        ScambiGUI(self.root)

    def open_infortuni(self):
        InfortuniMenuGUI(self.root)

    def open_visualizza_squadre(self):
        VisualizzaSquadreGUI(self.root)

    def open_visualizza_classifica(self):
        VisualizzaClassificaGUI(self.root)
    
    def open_eliminazione_squadra(self):
        EliminaSquadraGUI(self.root)
    
    def open_visualizza_giocatori(self):
        VisualizzaGiocatoriGUI(self.root)
    
    def open_inserisci_giocatore(self):
        InserisciGiocatoreGUI(self.root)

    def open_blocca_giocatore_espulso(self):
        BloccaSbloccaMenuGUI(self.root)

    def open_organizza_partite(self):
        OrganizzaPartiteGUI(self.root)
    
    def open_gestione_sponsor_squadra(self):
        GestioneSponsorSquadraGUI(self.root)
    
    def open_gestione_sponsor_torneo(self):
        GestioneSponsorTorneoGUI(self.root)
    
    def open_visualizza_calendario(self):
        VisualizzaCalendarioGUI(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = CampionatoApp(root)
    root.mainloop()
