from controls.TextLabel import TextLabel
from controls.TextEntry import TextEntry

def create_x_minmax_field(self):
    # Xmin label field
    x_min_label = TextLabel(self, text='Xmin')
    x_min_label.grid(row=4, column=0, padx=10, sticky="nw")

    # Xmin input field
    x_min_enter = TextEntry(self, self.plot.x_min)
    x_min_enter.grid(row=4, column=1, padx=10, sticky="ne")

    # Xmax label field
    x_max_label = TextLabel(self, text='Xmax')
    x_max_label.grid(row=5, column=0, padx=10, sticky="nw")

    # Xmax input field
    x_max_enter = TextEntry(self, self.plot.x_max)
    x_max_enter.grid(row=5, column=1, padx=10, sticky="ne")

def create_y_minmax_field(self):
    # Ymin label field
    y_min_label = TextLabel(self, text='Ymin')
    y_min_label.grid(row=6, column=0, padx=10, sticky="nw")

    # Ymin input field
    y_min_enter = TextEntry(self, self.plot.y_min)
    y_min_enter.grid(row=6, column=1, padx=10, sticky="ne")

    # Ymax label field
    y_max_label = TextLabel(self, text='Ymax')
    y_max_label.grid(row=7, column=0, padx=10, sticky="nw")

    # Ymax input field
    y_max_enter = TextEntry(self, self.plot.y_max)
    y_max_enter.grid(row=7, column=1, padx=10, sticky="ne")