import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.gui.visualizza_giocatori_gui import VisualizzaGiocatoriGUI
from app.services.scambi import scambio_giocatori

class ScambiGUI:
    def __init__(self, root, visualizza_giocatori_gui):
        self.root = tk.Toplevel(root)
        self.root.title("Proporre Scambio Giocatori")
        self.visualizza_giocatori_gui = visualizza_giocatori_gui
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        self.label_cf_offerto = ttk.Label(frame, text="CF Giocatore Offerto:")
        self.label_cf_offerto.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        
        self.entry_cf_offerto = ttk.Entry(frame)
        self.entry_cf_offerto.grid(column=1, row=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.label_squadra_offerta = ttk.Label(frame, text="Nome Squadra Offerta:")
        self.label_squadra_offerta.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
        
        self.entry_squadra_offerta = ttk.Entry(frame)
        self.entry_squadra_offerta.grid(column=1, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.label_cf_richiesto = ttk.Label(frame, text="CF Giocatore Richiesto:")
        self.label_cf_richiesto.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
        
        self.entry_cf_richiesto = ttk.Entry(frame)
        self.entry_cf_richiesto.grid(column=1, row=2, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.label_squadra_richiesta = ttk.Label(frame, text="Nome Squadra Richiesta:")
        self.label_squadra_richiesta.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
        
        self.entry_squadra_richiesta = ttk.Entry(frame)
        self.entry_squadra_richiesta.grid(column=1, row=3, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.btn_scambio = ttk.Button(frame, text="Proponi Scambio", command=self.proponi_scambio)
        self.btn_scambio.grid(column=0, row=4, columnspan=2, pady=10)

        self.result_label = ttk.Label(frame, text="")
        self.result_label.grid(column=0, row=5, columnspan=2, pady=5)

    def proponi_scambio(self):
        cf_offerto = self.entry_cf_offerto.get()
        squadra_offerta = self.entry_squadra_offerta.get()
        cf_richiesto = self.entry_cf_richiesto.get()
        squadra_richiesta = self.entry_squadra_richiesta.get()

        if cf_offerto and squadra_offerta and cf_richiesto and squadra_richiesta:
            connection = create_connection()
            if connection and connection.is_connected():
                success = scambio_giocatori(connection, cf_offerto, squadra_offerta, cf_richiesto, squadra_richiesta)
                connection.close()
                if success:
                    self.result_label.config(text="Scambio effettuato con successo!", foreground="green")
                    self.visualizza_giocatori_gui.aggiorna_visualizzazione()
                else:
                    self.result_label.config(text="Errore: Scambio non valido o non riuscito.", foreground="red")
            else:
                self.result_label.config(text="Connessione al database non riuscita", foreground="red")
        else:
            self.result_label.config(text="Tutti i campi sono obbligatori", foreground="red")

if __name__ == "__main__":
    root = tk.Tk()
    visualizza_giocatori_gui = VisualizzaGiocatoriGUI(root)
    ScambiGUI(root, visualizza_giocatori_gui)
    root.mainloop()
