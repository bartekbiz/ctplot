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

        # Create label
        label = tk.Label(self, text="Open CSV file to plot data", font=("Arial", 20))
        label.grid(row=0)

        open_button = tk.Button(
            master=self,
            text="Open CSV File",
            command=self.open_csv_file,
            bg="green",  # Background color
            fg="black",  # Foreground color
            font=("Arial", 15, "bold"),  # Font settings
            width=20,  # Width of the button
            height=2  # Height of the button
        )
        open_button.grid(row=1)

        close_button = tk.Button(
            master=self,
            text="Close Plot",
            command=self.close_plot,
            bg="red",  # Background color
            fg="black",  # Foreground color
            font=("Arial", 15, "bold"),  # Font settings
            width=20,  # Width of the button
            height=2  # Height of the button
        )
        close_button.grid(row=2)


        # change_file_button = tk.Button(
        #     master=self, text="Change CSV File", command=self.change_csv_file
        # )
        # change_file_button.grid(row=1, column=0)  # Place the change_file_button at (1, 0)

        # change_file_button.pack()


        self.protocol("WM_DELETE_WINDOW", self.destroy_plot)

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
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()

        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().grid(row=3, column=1, padx=20)  # Place the canvas at (3, 1)

        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()

        # placing the toolbar on the Tkinter window
        self.toolbar.grid(row=4, column=1)  # Place the toolbar at (4, 1)

    def close_plot(self):
        # Check if the canvas and toolbar exist
        if hasattr(self, 'canvas') or hasattr(self, 'toolbar'):
            # Destroy the canvas and toolbar
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
            del self.canvas
            del self.toolbar

        print("Close plot")

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

    def change_csv_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )

        if file_path:
            try:
                self.data["x"].clear()
                self.data["y"].clear()
                with open(file_path, "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        self.data["x"].append(float(row[0]))  # First column
                        self.data["y"].append(float(row[2]))  # Third column
                self.plot()

            except Exception as e:
                print(f"Error: {e}")

    def destroy_plot(self):
        print("Quitting...")
        self.destroy()
        exit()

    # def plot(self):
    #     # the figure that will contain the plot
    #     fig = Figure()
    #
    #     # adding the subplot
    #     fig, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True)
    #     ax1.plot(self.data["x"], self.data["y"])
    #     ax2.plot(self.data["x"], self.data["y"])
    #     ax3.plot(self.data["x"], self.data["y"])
    #
    #     # separate subplot titles
    #     ax1.set_title("Wykres x(t)")
    #     ax2.set_title("Wykres v(t)")
    #     ax3.set_title("Wykres a(t)")
    #
    #     ax1.set_ylabel("x [m]")
    #     ax2.set_ylabel("x [m]")
    #     ax3.set_ylabel("x [m]")
    #
    #     # common axis labels
    #     fig.supxlabel("t [s]")
    #
    #     # creating the Tkinter canvas
    #     # containing the Matplotlib figure
    #     canvas = FigureCanvasTkAgg(fig, master=self)
    #     canvas.draw()
    #
    #     # # placing the canvas on the Tkinter window
    #     # canvas.get_tk_widget().pack()
    #
    #     # placing the canvas on the Tkinter window
    #     canvas.get_tk_widget().grid(row=0, column=1)  # Place the canvas at (0, 1)
    #
    #     # creating the Matplotlib toolbar
    #     toolbar = NavigationToolbar2Tk(canvas, self)
    #     toolbar.update()
    #     # placing the toolbar on the Tkinter window
    #     toolbar.grid(row=1, column=1)  # Place the toolbar at (1, 1)
    #
    #     # # placing the toolbar on the Tkinter window
    #     # canvas.get_tk_widget().pack()

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
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()

        # placing the canvas on the Tkinter window
        self.canvas.get_tk_widget().grid(row=3, column=1, padx=20)  # Place the canvas at (3, 1)

        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()

        # placing the toolbar on the Tkinter window
        self.toolbar.grid(row=4, column=1)  # Place the toolbar at (4, 1)