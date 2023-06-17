import customtkinter as ctk
from main.homeview.frames import BottomHomeView, TopHomeFrame


class HomeView(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent)
        self.parent = parent
        self.pack_propagate(False)

        self.top_frame = TopHomeFrame(self)
        self.bottom_frame = BottomHomeView(self)

    def show(self) -> None:
        self.pack(fill="both", expand=True, side="left")

    def remove(self) -> None:
        self.pack_forget()
