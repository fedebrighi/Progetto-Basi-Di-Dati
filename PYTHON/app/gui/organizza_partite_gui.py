import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.organizza_partite import inserisci_partita, get_partite

class OrganizzaPartiteGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Organizza Partite")
        self.create_widgets()

    def create_widgets(self):
        self.label_giorno = ttk.Label(self.root, text="Giorno:")
        self.label_giorno.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
        self.entry_giorno = ttk.Entry(self.root, width=30)
        self.entry_giorno.grid(column=1, row=0, padx=10, pady=5)

        self.label_mese = ttk.Label(self.root, text="Mese:")
        self.label_mese.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
        self.entry_mese = ttk.Entry(self.root, width=30)
        self.entry_mese.grid(column=1, row=1, padx=10, pady=5)

        self.label_anno = ttk.Label(self.root, text="Anno:")
        self.label_anno.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
        self.entry_anno = ttk.Entry(self.root, width=30)
        self.entry_anno.grid(column=1, row=2, padx=10, pady=5)

        self.label_squadra_casa = ttk.Label(self.root, text="Squadra di Casa:")
        self.label_squadra_casa.grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
        self.entry_squadra_casa = ttk.Entry(self.root, width=30)
        self.entry_squadra_casa.grid(column=1, row=3, padx=10, pady=5)

        self.label_squadra_trasferta = ttk.Label(self.root, text="Squadra in Trasferta:")
        self.label_squadra_trasferta.grid(column=0, row=4, padx=10, pady=5, sticky=tk.W)
        self.entry_squadra_trasferta = ttk.Entry(self.root, width=30)
        self.entry_squadra_trasferta.grid(column=1, row=4, padx=10, pady=5)

        self.label_codice_stadio = ttk.Label(self.root, text="Codice Stadio:")
        self.label_codice_stadio.grid(column=0, row=5, padx=10, pady=5, sticky=tk.W)
        self.entry_codice_stadio = ttk.Entry(self.root, width=30)
        self.entry_codice_stadio.grid(column=1, row=5, padx=10, pady=5)

        self.label_codice_staff = ttk.Label(self.root, text="Codice Staff:")
        self.label_codice_staff.grid(column=0, row=6, padx=10, pady=5, sticky=tk.W)
        self.entry_codice_staff = ttk.Entry(self.root, width=30)
        self.entry_codice_staff.grid(column=1, row=6, padx=10, pady=5)

        self.label_codice_torneo = ttk.Label(self.root, text="Codice Torneo:")
        self.label_codice_torneo.grid(column=0, row=7, padx=10, pady=5, sticky=tk.W)
        self.entry_codice_torneo = ttk.Entry(self.root, width=30)
        self.entry_codice_torneo.grid(column=1, row=7, padx=10, pady=5)

        self.button_inserisci = ttk.Button(self.root, text="Inserisci Partita", command=self.inserisci_partita)
        self.button_inserisci.grid(column=0, row=8, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=9, columnspan=2, padx=10, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Giorno", "Mese", "Anno", "NomeCasa", "NomeOspite", "Risultato"), show="headings")
        self.tree.heading("Giorno", text="Giorno")
        self.tree.heading("Mese", text="Mese")
        self.tree.heading("Anno", text="Anno")
        self.tree.heading("NomeCasa", text="Squadra di Casa")
        self.tree.heading("NomeOspite", text="Squadra in Trasferta")
        self.tree.heading("Risultato", text="Risultato")
        self.tree.grid(column=0, row=10, columnspan=2, padx=10, pady=10, sticky=(tk.W, tk.E))

        self.button_aggiorna = ttk.Button(self.root, text="Aggiorna Visualizzazione", command=self.refresh_partite)
        self.button_aggiorna.grid(column=0, row=11, columnspan=2, padx=10, pady=10)

        self.refresh_partite()

    def inserisci_partita(self):
        giorno = self.entry_giorno.get()
        mese = self.entry_mese.get()
        anno = self.entry_anno.get()
        squadra_casa = self.entry_squadra_casa.get()
        squadra_trasferta = self.entry_squadra_trasferta.get()
        codice_stadio = self.entry_codice_stadio.get()
        codice_staff = self.entry_codice_staff.get()
        cod_torneo = self.entry_codice_torneo.get()

        if giorno and mese and anno and squadra_casa and squadra_trasferta and codice_stadio and codice_staff and cod_torneo:
            connection = create_connection()
            if connection and connection.is_connected():
                successo = inserisci_partita(connection, giorno, mese, anno, squadra_casa, squadra_trasferta, codice_stadio, codice_staff, cod_torneo)
                connection.close()
                if successo:
                    self.result_label.config(text="Partita inserita con successo!", foreground="green")
                    self.refresh_partite()
                else:
                    self.result_label.config(text="Errore durante l'inserimento della partita.", foreground="red")
            else:
                self.result_label.config(text="Connessione al database non riuscita.", foreground="red")
        else:
            self.result_label.config(text="Tutti i campi sono obbligatori.", foreground="red")

    def refresh_partite(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        connection = create_connection()
        if connection and connection.is_connected():
            partite = get_partite(connection)
            connection.close()

            for partita in partite:
                self.tree.insert("", tk.END, values=partita)

if __name__ == "__main__":
    root = tk.Tk()
    OrganizzaPartiteGUI(root)
    root.mainloop()
