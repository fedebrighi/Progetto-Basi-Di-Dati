import tkinter as tk
from tkinter import ttk, messagebox
from app.db import create_connection
from app.services.visualizza_ricavi_torneo import get_totale_fondi_e_spese_torneo, get_ricavi_sponsor, get_contributi_televisioni

class VisualizzaRicaviTorneoGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Visualizza Ricavi Torneo")
        self.cod_torneo = None
        self.create_widgets()

    def create_widgets(self):
        self.label_cod_torneo = ttk.Label(self.root, text="Inserisci il codice del torneo:")
        self.label_cod_torneo.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)

        self.entry_cod_torneo = ttk.Entry(self.root)
        self.entry_cod_torneo.grid(column=1, row=0, padx=10, pady=5, sticky=tk.W)

        self.button_salva_codice = ttk.Button(self.root, text="Salva Codice", command=self.salva_codice)
        self.button_salva_codice.grid(column=2, row=0, padx=10, pady=5, sticky=tk.W)

        self.label_totale_fondi = ttk.Label(self.root, text="Totale Fondi Torneo: ")
        self.label_totale_fondi.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
        
        self.label_spese = ttk.Label(self.root, text="Spese del Torneo: ")
        self.label_spese.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
        
        self.label_ricavi_sponsor = ttk.Label(self.root, text="Ricavi dagli Sponsor: ")
        self.label_ricavi_sponsor.grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
        
        self.label_contributi_televisioni = ttk.Label(self.root, text="Contributi delle Televisioni: ")
        self.label_contributi_televisioni.grid(column=0, row=4, padx=10, pady=5, sticky=tk.W)

        self.label_totale_finale = ttk.Label(self.root, text="Ricavi Torneo: ", foreground="green")
        self.label_totale_finale.grid(column=0, row=5, padx=10, pady=10, sticky=tk.W)

    def salva_codice(self):
        self.cod_torneo = self.entry_cod_torneo.get()
        if self.cod_torneo:
            self.refresh_ricavi()
        else:
            messagebox.showerror("Errore", "Inserisci un codice del torneo valido.")

    def refresh_ricavi(self):
        if not self.cod_torneo:
            messagebox.showerror("Errore", "Codice del torneo non inserito.")
            return

        connection = create_connection()
        if connection and connection.is_connected():
            totale_fondi, spese = get_totale_fondi_e_spese_torneo(connection, self.cod_torneo)
            ricavi_sponsor = get_ricavi_sponsor(connection, self.cod_torneo)
            contributi_televisioni = get_contributi_televisioni(connection, self.cod_torneo)

            try:
                # Convertire i valori in numeri
                totale_fondi = float(totale_fondi)
                spese = float(spese)
                ricavi_sponsor = float(ricavi_sponsor)
                contributi_televisioni = float(contributi_televisioni)

                totale_finale = totale_fondi - spese + ricavi_sponsor + contributi_televisioni

                print(f"Totale fondi: {totale_fondi}, Spese: {spese}, Ricavi sponsor: {ricavi_sponsor}, Contributi televisioni: {contributi_televisioni}")

                self.label_totale_fondi.config(text=f"Totale Fondi Torneo: {totale_fondi} €")
                self.label_spese.config(text=f"Spese del Torneo: {spese} €")
                self.label_ricavi_sponsor.config(text=f"Ricavi dagli Sponsor: {ricavi_sponsor} €")
                self.label_contributi_televisioni.config(text=f"Contributi delle Televisioni: {contributi_televisioni} €")
                self.label_totale_finale.config(text=f"Ricavi Torneo: {totale_finale} €")
            except ValueError as e:
                messagebox.showerror("Errore", f"Errore nella conversione dei dati: {e}")
                print(f"Errore nella conversione dei dati: {e}")

            connection.close()
        else:
            messagebox.showerror("Errore", "Connessione al database non riuscita.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VisualizzaRicaviTorneoGUI(root)
    root.mainloop()
