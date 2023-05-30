import customtkinter as ctk


class ProductsView(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, fg_color="red")
        self.parent = parent
        self.pack_propagate(False)

        self.pack(fill="both", expand=True)
