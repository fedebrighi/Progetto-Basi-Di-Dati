import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from app.db import create_connection
from app.services.visualizza_calendario import get_partite
import datetime

class VisualizzaCalendarioGUI:
    def __init__(self, root):
        self.root = tk.Toplevel(root)
        self.root.title("Visualizza Calendario Partite")
        self.create_widgets()

    def create_widgets(self):
        self.cal = Calendar(self.root, selectmode='day', year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day)
        self.cal.pack(pady=20)

        self.view_button = ttk.Button(self.root, text="Visualizza Partite", command=self.view_partite)
        self.view_button.pack(pady=10)

        self.partite_frame = ttk.Frame(self.root)
        self.partite_frame.pack(pady=20, fill="both", expand=True)
        
        self.tree = ttk.Treeview(self.partite_frame, columns=("Squadra Casa", "Squadra Trasferta", "Data", "Ora"), show='headings')
        self.tree.heading("Squadra Casa", text="Squadra Casa")
        self.tree.heading("Squadra Trasferta", text="Squadra Trasferta")
        self.tree.heading("Data", text="Data")
        self.tree.pack(fill="both", expand=True)

        self.load_partite_into_calendar()

    def load_partite_into_calendar(self):
        connection = create_connection()
        if not connection or not connection.is_connected():
            print("Connessione al database non riuscita")
            return

        partite = get_partite(connection)
        for partita in partite:
            data_partita = datetime.date(int(partita[4]), int(partita[3]), int(partita[2]))
            self.cal.calevent_create(data_partita, f"{partita[0]} vs {partita[1]}", "partita")

        connection.close()

    def view_partite(self):
        connection = create_connection()
        if not connection or not connection.is_connected():
            print("Connessione al database non riuscita")
            return

        partite = get_partite(connection)

        for row in self.tree.get_children():
            self.tree.delete(row)

        selected_date = self.cal.selection_get()
        for partita in partite:
            data_partita = datetime.date(int(partita[4]), int(partita[3]), int(partita[2]))
            if data_partita == selected_date:
                self.tree.insert("", tk.END, values=(partita[0], partita[1], data_partita, partita[5]))

        connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = VisualizzaCalendarioGUI(root)
    root.mainloop()
