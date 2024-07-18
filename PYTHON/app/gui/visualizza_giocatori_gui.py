import tkinter as tk
from tkinter import ttk
from app.db import create_connection, fetch_query

class VisualizzaGiocatoriGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Visualizza Giocatori")
        self.create_widgets()
        self.nome_squadra = ""

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        self.label_nome_squadra = ttk.Label(frame, text="Nome Squadra:")
        self.label_nome_squadra.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        
        self.entry_nome_squadra = ttk.Entry(frame)
        self.entry_nome_squadra.grid(column=1, row=0, padx=5, pady=5, sticky=(tk.W, tk.E))
        
        self.btn_cerca = ttk.Button(frame, text="Cerca", command=self.visualizza_giocatori)
        self.btn_cerca.grid(column=2, row=0, padx=5, pady=5)

        self.result_label = ttk.Label(frame, text="")
        self.result_label.grid(column=0, row=1, columnspan=3, pady=5)

        self.tree = ttk.Treeview(frame, columns=("Nome", "Cognome", "Numero", "Ruolo"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Cognome", text="Cognome")
        self.tree.heading("Numero", text="Numero di Maglia")
        self.tree.heading("Ruolo", text="Ruolo")
        self.tree.grid(column=0, row=2, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        frame.rowconfigure(2, weight=1)

    def visualizza_giocatori(self):
        self.nome_squadra = self.entry_nome_squadra.get()
        print(f"Visualizza giocatori per la squadra: {self.nome_squadra}")
        self.aggiorna_visualizzazione()

    def aggiorna_visualizzazione(self):
        if self.nome_squadra:
            connection = create_connection()
            if connection and connection.is_connected():
                query = """
                SELECT g.Nome, g.Cognome, n.Numero, n.Ruolo 
                FROM giocatore g
                JOIN numero n ON g.CodiceFiscale = n.CodiceFiscale
                WHERE n.NomeSquadra = %s
                ORDER BY n.Numero DESC
                """
                values = (self.nome_squadra,)
                print(f"Eseguendo query: {query} con valori: {values}")
                giocatori = fetch_query(connection, query, values)
                if giocatori:
                    print(f"Trovati {len(giocatori)} giocatori per la squadra {self.nome_squadra}")
                    self.result_label.config(text=f"Giocatori della squadra '{self.nome_squadra}':", foreground="green")
                    for i in self.tree.get_children():
                        self.tree.delete(i)
                    for giocatore in giocatori:
                        self.tree.insert("", tk.END, values=giocatore)
                        print(f"Inserito giocatore: {giocatore}")
                else:
                    print(f"Nessun giocatore trovato per la squadra {self.nome_squadra}")
                    self.result_label.config(text=f"Errore: La squadra '{self.nome_squadra}' non esiste o non ha giocatori.", foreground="red")
                connection.close()
                print("Connessione chiusa correttamente")
            else:
                print("Connessione al database non riuscita")
                self.result_label.config(text="Connessione al database non riuscita", foreground="red")
        else:
            print("Nome della squadra non inserito")
            self.result_label.config(text="Inserisci il nome di una squadra", foreground="red")

if __name__ == "__main__":
    root = tk.Tk()
    VisualizzaGiocatoriGUI(root)
    root.mainloop()
