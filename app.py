import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CTPlot")

        # geometry fields
        self.w_width = 960
        self.w_height = 720
        self.geometry(f"{self.w_width}x{self.w_height}")

        # plot fields
        self.data = {"x": [], "y": []}
        self.canvas = None
        self.toolbar = None
        self.is_button_disabled = tk.DISABLED
        self.x_min = tk.DoubleVar()
        self.x_max = tk.DoubleVar()
        self.y_min = tk.DoubleVar()
        self.y_max = tk.DoubleVar()

        # Create label
        label = tk.Label(self, text="Open CSV file to plot data", font=("Arial", 18))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        open_button = tk.Button(
            master=self,
            text="Open CSV File",
            command=self.open_csv_file,
            font=("Arial", 15, "bold"),
            width=20,
            height=2
        )
        open_button.grid(row=1, column=0, padx=10, sticky="nw")

        self.close_button = tk.Button(
            master=self,
            text="Close Plot",
            command=self.close_plot,
            font=("Arial", 15, "bold"),
            width=20,
            height=2,
            state=self.is_button_disabled
        )
        self.close_button.grid(row=2, column=0, padx=10, sticky="nw")

        # Xmin label field
        x_min_label = tk.Label(self, text='Xmin', font=('calibre', 10, 'bold'), width=5, justify='center',
                               relief='solid', bd=1, bg='white', fg='black', highlightthickness=2)
        x_min_label.grid(row=3, column=0, padx=10, sticky="nw")

        # Xmin input field
        x_min_enter = tk.Entry(self, textvariable=self.x_min, font=('calibre', 10, 'normal'), width=10,
                               justify='center', relief='solid', bd=1, bg='white', fg='black', highlightcolor='blue',
                               highlightthickness=1, insertbackground='black', selectbackground='blue',
                               selectforeground='white')
        x_min_enter.place(x=70, y=141)

        # Xmax label field
        x_max_label = tk.Label(self, text='Xmax', font=('calibre', 10, 'bold'), width=5, justify='center',
                               relief='solid', bd=1, bg='white', fg='black', highlightthickness=2)
        x_max_label.grid(row=4, column=0,  padx=10, sticky="nw")

        # Xmax input field
        x_max_enter = tk.Entry(self, textvariable=self.x_max, font=('calibre', 10, 'normal'), width=10,
                               justify='center', relief='solid', bd=1, bg='white', fg='black', highlightcolor='blue',
                               highlightthickness=1, insertbackground='black', selectbackground='blue',
                               selectforeground='white')
        x_max_enter.place(x=70, y=161)

        # Ymin label field
        y_min_label = tk.Label(self, text='Ymin', font=('calibre', 10, 'bold'), width=5, justify='center',
                               relief='solid', bd=1, bg='white', fg='black', highlightthickness=2)
        y_min_label.grid(row=5, column=0, padx=10, sticky="nw")

        # Ymin input field
        y_min_enter = tk.Entry(self, textvariable=self.y_min, font=('calibre', 10, 'normal'), width=10,
                               justify='center', relief='solid', bd=1, bg='white', fg='black', highlightcolor='blue',
                               highlightthickness=1, insertbackground='black', selectbackground='blue',
                               selectforeground='white')
        y_min_enter.place(x=70, y=181)

        # Ymax label field
        y_max_label = tk.Label(self, text='Ymax', font=('calibre', 10, 'bold'), width=5, justify='center',
                               relief='solid', bd=1, bg='white', fg='black', highlightthickness=2)
        y_max_label.grid(row=6, column=0, padx=10, sticky="nw")

        # Ymax input field
        y_max_enter = tk.Entry(self, textvariable=self.y_max, font=('calibre', 10, 'normal'), width=10,
                               justify='center', relief='solid', bd=1, bg='white', fg='black', highlightcolor='blue',
                               highlightthickness=1, insertbackground='black', selectbackground='blue',
                               selectforeground='white')
        y_max_enter.place(x=70, y=201)

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
                # Clear data
                self.data["y"].clear()
                self.data["x"].clear()

                self.is_button_disabled = tk.NORMAL
                # Update the state of the close_button
                self.close_button.config(state=self.is_button_disabled)

            except Exception as e:
                print(f"Error: {e}")

    def close_plot(self):
        # Check if the canvas and toolbar exist
        if (self.canvas is not None and
                self.toolbar is not None):
            print("Closing plot...")

            # Destroy the canvas and toolbar
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
            self.canvas = None
            self.toolbar = None

        self.is_button_disabled = tk.DISABLED
        # Update the state of the close_button
        self.close_button.config(state=self.is_button_disabled)

    def create_plot(self):
        print("\nCreating plot...")

        # adding the subplot
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True)
        fig.set_figwidth(7)
        fig.set_figheight(6.6)

        ax1.plot(self.data["x"], self.data["y"])
        ax2.plot(self.data["x"], self.data["y"])
        ax3.plot(self.data["x"], self.data["y"])

        # Adding grids to plots
        ax1.grid()
        ax2.grid()
        ax3.grid()

        # separate subplot titles
        ax1.set_title("Wykres x(t)")
        ax2.set_title("Wykres v(t)")
        ax3.set_title("Wykres a(t)")

        ax1.set_ylabel("x [m]")
        ax2.set_ylabel("x [m]")
        ax3.set_ylabel("x [m]")

        # common axis labels
        fig.supxlabel("t [s]")

        # Set the minimum x-value for the plots
        ax1.set_xlim(left=self.x_min.get())
        ax2.set_xlim(left=self.x_min.get())
        ax3.set_xlim(left=self.x_min.get())

        # Set the maximum x-value for the plots
        ax1.set_xlim(right=self.x_max.get())
        ax2.set_xlim(right=self.x_max.get())
        ax3.set_xlim(right=self.x_max.get())

        # Set the minimum y-value for the plots
        ax1.set_ylim(bottom=self.y_min.get())
        ax2.set_ylim(bottom=self.y_min.get())
        ax3.set_ylim(bottom=self.y_min.get())

        # Set the maximum y-value for the plots
        ax1.set_ylim(top=self.y_max.get())
        ax2.set_ylim(top=self.y_max.get())
        ax3.set_ylim(top=self.y_max.get())

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=247, y=13)

        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.place(x=8, y=self.w_height - 40)

    def destroy_app(self):
        print("\nQuitting...")
        self.destroy()
        exit()
