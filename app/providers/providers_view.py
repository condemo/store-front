import customtkinter as ctk


class ProvidersView(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, fg_color="yellow")
        self.parent = parent
        self.pack_propagate(False)

    def show(self) -> None:
        self.pack(fill="both", expand=True, side="left")

    def remove(self) -> None:
        self.pack_forget()
