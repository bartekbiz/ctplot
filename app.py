import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("720x400")
        self.title("Plotting data from a CSV file")
        self.data = {'x': [], 'y': []}  

        open_button = tk.Button(self, text="Open CSV File", command=self.open_csv_file)
        open_button.pack()

    def open_csv_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        self.data['x'].append(float(row[0]))  # First column
                        self.data['y'].append(float(row[2]))  # Third column
                self.plot_data()
            except Exception as e:
                print(f"Error: {e}")

    def plot_data(self):
        plt.plot(self.data['x'], self.data['y'])
        plt.xlabel('t [s]')
        plt.ylabel('x [m]')
        plt.title('Wykres x(t)')
        plt.grid(True)
        plt.show()