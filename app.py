import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

import matplotlib.pyplot as plt

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        open_button = tk.Button(self, text="Open .csv File", command=self.open_csv_file)
        open_button.pack()
        
        self.title('ctplot')
        self.create_figure()

    def create_figure(self):
        # prepare data
        data = {
            'Python': 11.27,
            'C': 11.16,
            'Java': 10.46,
            'C++': 7.5,
            'C#': 5.26
        }
        languages = data.keys()
        popularity = data.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(languages, popularity)
        axes.set_title('Top 5 Programming Languages')
        axes.set_ylabel('Popularity')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def open_csv_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        print(row)
            except Exception as e:
                print(f"Error: {e}")