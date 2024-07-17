import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.elimina_squadra import elimina_squadra
from app.db import fetch_query

class EliminaSquadraGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Elimina Squadra")
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Nome squadra da eliminare:")
        self.label.pack(pady=10)

        self.nome_squadra_entry = ttk.Entry(self.root)
        self.nome_squadra_entry.pack(pady=10)

        self.elimina_button = ttk.Button(self.root, text="Elimina Squadra", command=self.elimina_squadra)
        self.elimina_button.pack(pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)

    def elimina_squadra(self):
        nome_squadra = self.nome_squadra_entry.get()
        if nome_squadra:
            connection = create_connection()
            if connection and connection.is_connected():
                query_check = "SELECT COUNT(*) FROM squadra WHERE Nome = %s"
                result = fetch_query(connection, query_check, (nome_squadra,))
                if result[0][0] == 0:
                    self.result_label.config(text=f"Errore: La squadra '{nome_squadra}' non esiste nel database.", foreground="red")
                    connection.close()
                    return
                
                elimina_squadra(connection, nome_squadra)
                connection.close()
                self.result_label.config(text=f"Squadra '{nome_squadra}' eliminata con successo.", foreground="green")
            else:
                self.result_label.config(text="Connessione al database non riuscita", foreground="red")
        else:
            self.result_label.config(text="Inserisci il nome di una squadra", foreground="red")

if __name__ == "__main__":
    root = tk.Tk()
    EliminaSquadraGUI(root)
    root.mainloop()
