from controls.base.Separator import Separator


class UnderButtonsSeparator(Separator):
    def __init__(self, app):
        super().__init__(app)
        self.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")


class UnderEverythingSeparator(Separator):
    def __init__(self, app):
        super().__init__(app)
        self.grid(row=100, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
