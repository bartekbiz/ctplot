import csv

from tkinter import filedialog
from controls.base.LargeButton import LargeButton


class OpenCSVButton(LargeButton):
    def __init__(self, app):
        self.app = app

        super().__init__(
            self.app,
            text="Open CSV File",
            command=self.open
        )

        self.grid(row=2, column=0, columnspan=2, padx=10, sticky="nw")
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
                csv_reader = csv.reader(csv_file)
                self.app.current_module.data["x"].clear()
                self.app.current_module.data["y"].clear()

                for row in csv_reader:
                    self.app.current_module.data["x"].append(float(row[0]))
                    self.app.current_module.data["y"].append(float(row[1])/1000)

            self.app.current_module.plot.create_plot()

            self.app.close_button.set_is_disabled(False)

        except Exception as e:
            print(f"Error: {e}")
   