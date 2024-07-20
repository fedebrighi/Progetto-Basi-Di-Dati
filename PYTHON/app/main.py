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
from app.gui.visualizza_calendario_gui import VisualizzaCalendarioGUI
from app.gui.gestione_sponsor_squadra_gui import GestioneSponsorSquadraGUI
from app.services.retrocessione import retrocessione_squadre
from app.db import create_connection

class CampionatoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campionato Manager")
        self.root.geometry("800x600")
        self.visualizza_giocatori_gui = None  # Non creare l'istanza qui
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)

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

        self.btn_iscrizione = ttk.Button(main_frame, text="Iscrizione Squadra", command=self.open_iscrizione)
        self.btn_iscrizione.grid(column=0, row=2, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_scambio = ttk.Button(main_frame, text="Proporre Scambio Giocatori", command=self.open_scambi)
        self.btn_scambio.grid(column=1, row=2, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_infortunio = ttk.Button(main_frame, text="Infortuni", command=self.open_infortuni)
        self.btn_infortunio.grid(column=0, row=3, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_visualizza_squadre = ttk.Button(main_frame, text="Visualizza Squadre", command=self.open_visualizza_squadre)
        self.btn_visualizza_squadre.grid(column=1, row=3, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_visualizza_classifica = ttk.Button(main_frame, text="Visualizza Classifica", command=self.open_visualizza_classifica)
        self.btn_visualizza_classifica.grid(column=0, row=4, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_eliminazione_squadra = ttk.Button(main_frame, text="Eliminazione Squadra", command=self.open_eliminazione_squadra)
        self.btn_eliminazione_squadra.grid(column=1, row=4, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_visualizza_giocatori = ttk.Button(main_frame, text="Visualizza Giocatori", command=self.open_visualizza_giocatori)
        self.btn_visualizza_giocatori.grid(column=0, row=5, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_inserisci_giocatore = ttk.Button(main_frame, text="Inserisci Giocatori nelle Squadre", command=self.open_inserisci_giocatore)
        self.btn_inserisci_giocatore.grid(column=1, row=5, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_blocca_giocatore_espulso = ttk.Button(main_frame, text="Blocca/Sblocca Giocatore Espulso", command=self.open_blocca_giocatore_espulso)
        self.btn_blocca_giocatore_espulso.grid(column=0, row=6, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_organizza_partite = ttk.Button(main_frame, text="Organizzazione Partite tra Squadre", command=self.open_organizza_partite)
        self.btn_organizza_partite.grid(column=1, row=6, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_gestione_sponsor_squadra = ttk.Button(main_frame, text="Gestione Sponsor Squadra", command=self.open_gestione_sponsor_squadra)
        self.btn_gestione_sponsor_squadra.grid(column=0, row=7, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_gestione_sponsor_torneo = ttk.Button(main_frame, text="Gestione Sponsor Torneo", command=self.open_gestione_sponsor_torneo)
        self.btn_gestione_sponsor_torneo.grid(column=1, row=7, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_visualizza_ricavi_torneo = ttk.Button(main_frame, text="Visualizza Ricavi Torneo", command=self.open_visualizza_ricavi_torneo)
        self.btn_visualizza_ricavi_torneo.grid(column=0, row=8, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.btn_visualizza_calendario = ttk.Button(main_frame, text="Visualizza Calendario Partite", command=self.open_visualizza_calendario)
        self.btn_visualizza_calendario.grid(column=1, row=8, padx=10, pady=10, sticky=(tk.W, tk.E))
        
        self.btn_retrocessione = ttk.Button(main_frame, text="Controlla Retrocessioni", command=self.controlla_retrocessioni)
        self.btn_retrocessione.grid(column=0, row=9, columnspan=2, padx=10, pady=10, sticky=(tk.W, tk.E))

    def open_iscrizione(self):
        IscrizioneGUI(self.root)

    def open_scambi(self):
        if not self.visualizza_giocatori_gui:
            self.visualizza_giocatori_gui = VisualizzaGiocatoriGUI(self.root)
        ScambiGUI(self.root, self.visualizza_giocatori_gui)

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

    def open_visualizza_ricavi_torneo(self):
        VisualizzaRicaviTorneoGUI(self.root)
    
    def open_visualizza_calendario(self):
        VisualizzaCalendarioGUI(self.root)
        
    def controlla_retrocessioni(self):
        connection = create_connection()
        if connection and connection.is_connected():
            retrocessione_squadre(connection)
            connection.close()
        else:
            print("Connessione al database non riuscita")

if __name__ == "__main__":
    root = tk.Tk()
    app = CampionatoApp(root)
    root.mainloop()
