import tkinter as tk
from tkinter import ttk
from app.db import create_connection, fetch_query

def get_giocatori_per_squadra(connection, nome_squadra):
    query = """
    SELECT g.Nome, g.Cognome, n.Numero, n.Ruolo
    FROM giocatore g
    JOIN numero n ON g.CodiceFiscale = n.CodiceFiscale
    JOIN squadra s ON g.NomeSquadra = s.Nome
    WHERE s.Nome = %s
    ORDER BY n.Numero DESC
    """
    values = (nome_squadra,)
    return fetch_query(connection, query, values)

class VisualizzaGiocatoriGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Visualizza Giocatori")
        self.create_widgets()

    def create_widgets(self):
        self.label_squadra = tk.Label(self.root, text="Nome Squadra:")
        self.label_squadra.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
        
        self.entry_squadra = ttk.Entry(self.root, width=30)
        self.entry_squadra.grid(column=1, row=0, padx=10, pady=5)

        self.btn_visualizza = ttk.Button(self.root, text="Visualizza Giocatori", command=self.visualizza_giocatori)
        self.btn_visualizza.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Nome", "Cognome", "Numero", "Ruolo"), show="headings")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Cognome", text="Cognome")
        self.tree.heading("Numero", text="Numero")
        self.tree.heading("Ruolo", text="Ruolo")
        self.tree.grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky=(tk.W, tk.E))

    def visualizza_giocatori(self):
        nome_squadra = self.entry_squadra.get()

        connection = create_connection()
        if connection and connection.is_connected():
            giocatori = get_giocatori_per_squadra(connection, nome_squadra)
            
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            if giocatori:  # Verifica se giocatori non è None
                for giocatore in giocatori:
                    self.tree.insert("", tk.END, values=giocatore)
                
            connection.close()

    def aggiorna_visualizzazione(self):
        self.visualizza_giocatori()

if __name__ == "__main__":
    root = tk.Tk()
    VisualizzaGiocatoriGUI(root)
    root.mainloop()
