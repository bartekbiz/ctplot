import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1080x720")
        self.title("Plotting data from a CSV file")
        self.data = {"x": [], "y": []}
        self.canvas = None
        self.toolbar = None

        # Create label
        label = tk.Label(self, text="Open CSV file to plot data", font=("Arial", 20))
        label.grid(row=0, column=0)

        open_button = tk.Button(
            master=self,
            text="Open CSV File",
            command=self.open_csv_file,
            font=("Arial", 15, "bold"),
            width=20,
            height=2
        )
        open_button.grid(row=1, column=0)

        close_button = tk.Button(
            master=self,
            text="Close Plot",
            command=self.close_plot,
            font=("Arial", 15, "bold"),
            width=20,
            height=2
        )
        close_button.grid(row=2, column=0)

        self.protocol("WM_DELETE_WINDOW", self.destroy_app)

    def open_csv_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )

        if file_path:
            try:
                with open(file_path, "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        self.data["x"].append(float(row[0]))
                        self.data["y"].append(float(row[2]))
                self.create_plot()

            except Exception as e:
                print(f"Error: {e}")

    def close_plot(self):
        # Check if the canvas and toolbar exist
        if (self.canvas is not None and
                self.toolbar is not None):
            print("Closing plot...")

            # Clear data
            self.data["x"].clear()
            self.data["y"].clear()

            # Destroy the canvas and toolbar
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
            self.canvas = None
            self.toolbar = None

    def create_plot(self):
        print("Creating plot...")

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
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()

        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().place(relx=0.24, y=0)

        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()

        # placing the toolbar on the Tkinter window
        self.toolbar.place(relx=0, rely=0.95)

    def destroy_app(self):
        print("Quitting...")
        self.destroy()
        exit()
