import customtkinter as ctk
from data.preload import DataLoadCache
from config import DATA_URL


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("1400x800+750+80")
        self.title("Store Management")

        DataLoadCache(DATA_URL)
