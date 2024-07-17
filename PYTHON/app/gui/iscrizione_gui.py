import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.iscrizione_squadra import iscrizione_squadra

class IscrizioneGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Iscrizione Squadra")
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Labels and Entry widgets
        ttk.Label(frame, text="Nome Squadra:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_nome = ttk.Entry(frame)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Anno Fondazione:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_anno = ttk.Entry(frame)
        self.entry_anno.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Città Riferimento:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_citta = ttk.Entry(frame)
        self.entry_citta.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Quota Iscrizione:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_quota = ttk.Entry(frame)
        self.entry_quota.grid(row=3, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        ttk.Label(frame, text="Trofei Vinti:").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_trofei = ttk.Entry(frame)
        self.entry_trofei.grid(row=4, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Iscrivi button
        self.button_iscrivi = ttk.Button(frame, text="Iscrivi", command=self.iscrivi_squadra)
        self.button_iscrivi.grid(row=5, column=0, columnspan=2, pady=10)

        # Result label
        self.result_label = ttk.Label(frame, text="")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=5)

        # Configure column weight for resizing
        frame.columnconfigure(1, weight=1)

    def iscrivi_squadra(self):
        nome = self.entry_nome.get()
        anno = self.entry_anno.get()
        citta = self.entry_citta.get()
        quota = self.entry_quota.get()
        trofei = self.entry_trofei.get()

        if nome and anno and citta and quota and trofei:
            connection = create_connection()
            if connection and connection.is_connected():
                iscrizione_squadra(connection, nome, anno, citta, quota, trofei)
                connection.close()
                self.result_label.config(text="Squadra iscritta con successo!", foreground="green")
            else:
                self.result_label.config(text="Connessione al database non riuscita", foreground="red")
        else:
            self.result_label.config(text="Tutti i campi sono obbligatori", foreground="red")

if __name__ == "__main__":
    root = tk.Tk()
    IscrizioneGUI(root)
    root.mainloop()
