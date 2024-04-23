import csv

from tkinter import filedialog
from controls.base.LargeButton import LargeButton


class OpenCSVButton(LargeButton):
    def __init__(self, window, module, row, col=0):
        self.module = module

        super().__init__(
            window,
            text="Open CSV File",
            command=self.open
        )

        self.grid(row=row, column=col, columnspan=2, padx=10, sticky="nw")
        self.focus()
        self.bind("<Return>", self.open)

    def open(self, *event):
        file_path = filedialog.askopenfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )

        if not file_path:
            return

        try:
            with open(file_path, "r", encoding='utf-8-sig') as csv_file:
                sample_line = csv_file.readline()
                delimiter = ',' if ',' in sample_line else ';'

                csv_file.seek(0)

                csv_reader = csv.reader(csv_file, delimiter=delimiter)
                self.module.data["x"].clear()
                self.module.data["y"].clear()

                for row in csv_reader:
                    self.module.data["x"].append(float(row[0]))
                    self.module.data["y"].append(float(row[1])) 

            self.module.plot.create_plot()

            self.module.close_button.set_is_disabled(False)

        except Exception as e:
            print(f"Error: {e}")
   