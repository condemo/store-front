import customtkinter as ctk

from lib import View
from utils import ViewController
from products import ProductsView
from providers import ProvidersView
from main.homeview import HomeView


class MainMenu(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, width=50)
        self.parent = parent
        self.pack_propagate(False)
        self.menu_btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.load_buttons()

        self.menu_btn_frame.pack(expand=True)

        self.pack(side="left", fill="y")
        self.view_controller = ViewController(ProductsView(self.parent))

    def load_view(self, view: View) -> None:
        self.view_controller.change_view(view)

    def load_buttons(self) -> None:
        self.products_btn = ctk.CTkButton(
            self.menu_btn_frame,
            text="1", width=40,
            command=lambda: self.load_view(ProductsView(self.parent)))
        self.home_btn = ctk.CTkButton(
            self.menu_btn_frame,
            text="2", width=40,
            command=lambda: self.load_view(HomeView(self.parent)))
        self.providers_btn = ctk.CTkButton(
            self.menu_btn_frame,
            text="3", width=40,
            command=lambda: self.load_view(ProvidersView(self.parent)))

        self.products_btn.pack(pady=5)
        self.home_btn.pack(pady=5)
        self.providers_btn.pack(pady=5)
