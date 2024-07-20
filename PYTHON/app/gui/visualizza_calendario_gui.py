import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from app.db import create_connection
import datetime

class VisualizzaCalendarioGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Visualizza Calendario Partite")
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill="both", expand=True)

        self.cal_frame = ttk.Frame(main_frame)
        self.cal_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        self.cal = Calendar(self.cal_frame, selectmode='day', year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day)
        self.cal.pack(expand=True)

        self.view_button = ttk.Button(main_frame, text="Visualizza Partite", command=self.view_partite)
        self.view_button.pack(pady=10)

        self.partite_frame = ttk.Frame(main_frame)
        self.partite_frame.pack(side="bottom", fill="x", expand=False, padx=20, pady=10)
        
        self.tree = ttk.Treeview(self.partite_frame, columns=("Squadra Casa", "Squadra Trasferta", "Data", "Risultato"), show='headings', height=5)
        self.tree.heading("Squadra Casa", text="Squadra Casa")
        self.tree.heading("Squadra Trasferta", text="Squadra Trasferta")
        self.tree.heading("Data", text="Data")
        self.tree.heading("Risultato", text="Risultato")
        self.tree.pack(fill="x", expand=True)

        self.load_partite_into_calendar()

    def load_partite_into_calendar(self):
        connection = create_connection()
        if not connection or not connection.is_connected():
            print("Connessione al database non riuscita")
            return

        query = "SELECT NomeCasa, NomeOspite, Giorno, Mese, Anno FROM partita"
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            partite = cursor.fetchall()
            for partita in partite:
                data_partita = datetime.date(int(partita[4]), int(partita[3]), int(partita[2]))
                self.cal.calevent_create(data_partita, f"{partita[0]} vs {partita[1]}", "partita")
            cursor.close()
        except Exception as e:
            print(f"Errore durante il recupero delle partite: {e}")

        connection.close()

    def view_partite(self):
        connection = create_connection()
        if not connection or not connection.is_connected():
            print("Connessione al database non riuscita")
            return

        query = "SELECT NomeCasa, NomeOspite, Giorno, Mese, Anno, Risultato FROM partita"
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            partite = cursor.fetchall()
            
            for row in self.tree.get_children():
                self.tree.delete(row)

            selected_date = self.cal.selection_get()
            for partita in partite:
                data_partita = datetime.date(int(partita[4]), int(partita[3]), int(partita[2]))
                if data_partita == selected_date:
                    self.tree.insert("", tk.END, values=(partita[0], partita[1], data_partita, partita[5]))

            cursor.close()
        except Exception as e:
            print(f"Errore durante il recupero delle partite: {e}")

        connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = VisualizzaCalendarioGUI(root)
    root.mainloop()
