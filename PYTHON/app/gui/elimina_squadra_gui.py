import tkinter as tk
from tkinter import ttk
from app.db import create_connection
from app.services.elimina_squadra import elimina_squadra
from app.db import fetch_query

class EliminaSquadraGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Eliminazione Squadra")
        self.create_widgets()

    def create_widgets(self):
        self.label_nome_squadra = ttk.Label(self.root, text="Nome Squadra:")
        self.label_nome_squadra.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
        self.entry_nome_squadra = ttk.Entry(self.root, width=30)
        self.entry_nome_squadra.grid(column=1, row=0, padx=10, pady=5)

        self.button_elimina = ttk.Button(self.root, text="Elimina Squadra", command=self.elimina_squadra)
        self.button_elimina.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    def elimina_squadra(self):
        nome_squadra = self.entry_nome_squadra.get()
        connection = create_connection()
        if not connection or not connection.is_connected():
            self.result_label.config(text="Connessione al database non riuscita", foreground="red")
            return

        elimina_squadra(connection, nome_squadra)
        connection.close()

        self.result_label.config(text=f"Squadra {nome_squadra} eliminata con successo.", foreground="green")

if __name__ == "__main__":
    root = tk.Tk()
    EliminaSquadraGUI(root)
    root.mainloop()
