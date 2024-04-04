import tkinter as tk
from tkinter import filedialog
import csv
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1080x720")
        self.title("Plotting data from a CSV file")
        self.data = {"x": [], "y": []}

        open_button = tk.Button(
            master=self, text="Open CSV File", command=self.open_csv_file
        )
        open_button.pack()

    def open_csv_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )

        if file_path:
            try:
                with open(file_path, "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        self.data["x"].append(float(row[0]))  # First column
                        self.data["y"].append(float(row[2]))  # Third column
                self.plot()

            except Exception as e:
                print(f"Error: {e}")

    def plot_data(self):
        plt.plot()
        plt.xlabel("t [s]")
        plt.ylabel("x [m]")
        plt.title("Wykres x(t)")
        plt.grid(True)
        # plt.show()

    def plot(self):

        # the figure that will contain the plot
        fig = Figure()

        # adding the subplot
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True)
        ax1.plot(self.data["x"], self.data["y"])
        ax2.plot(self.data["x"], self.data["y"])
        ax3.plot(self.data["x"], self.data["y"])

        # separate subplot titles
        ax1.set_title("Wykres x(t)")
        ax2.set_title("Wykres v(t)")
        ax3.set_title("Wykres a(t)")

        ax1.set_ylabel("x [m]")
        ax2.set_ylabel("x [m]")
        ax3.set_ylabel("x [m]")

        # common axis labels
        fig.supxlabel("t [s]")

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()
