from controls.base.Separator import Separator


class UnderButtonsSeparator(Separator):
    def __init__(self, module):
        super().__init__(module.app)
        self.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")


class UnderEverythingSeparator(Separator):
    def __init__(self, module):
        super().__init__(module.app)
        self.grid(row=100, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
