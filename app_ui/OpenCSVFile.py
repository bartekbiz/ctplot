import tkinter as tk
from tkinter import filedialog
from tkinter import filedialog
import csv


class OpenCSVFile():
    def __init__(self, app):
        self.app = app

    def open(self, *event):
        file_path = filedialog.askopenfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )

        if file_path:
            try:
                with open(file_path, "r", encoding='utf-8-sig') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    self.app.data["x"].clear()
                    self.app.data["y"].clear()

                    for row in csv_reader:
                        self.app.data["x"].append(float(row[0]))
                        self.app.data["y"].append(float(row[1])/1000)

                self.app.plot.create_plot()

                self.app.close_button.set_is_disabled(False)

            except Exception as e:
                print(f"Error: {e}")
   