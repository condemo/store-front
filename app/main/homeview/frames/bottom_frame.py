import customtkinter as ctk


class BottomHomeView(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, fg_color="orange")
        self.pack_propagate(False)

        self.pack(expand=True, fill="both")
