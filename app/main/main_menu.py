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
        self.menu_btn_frame = ctk.CTkFrame(self, fg_color="transparent")  # Menu Btn Frame
        self.load_buttons()  # Loads al view butttons
        self.current_btn_press = self.home_btn  # Set de home btn by default
        self.home_btn.configure(state="disabled")  # Disable the home btn

        self.menu_btn_frame.pack(expand=True)
        self.pack(side="left", fill="y")

        self.view_controller = ViewController(HomeView(self.parent))

    def load_view(self, view: View, btn) -> None:
        self.view_controller.change_view(view)  # Loads new view

        # Changes de btn state
        self.current_btn_press.configure(state="normal")
        self.current_btn_press = btn
        self.current_btn_press.configure(state="disabled")

    def load_buttons(self) -> None:
        self.products_btn = ctk.CTkButton(
            self.menu_btn_frame,
            text="1", width=40,
            command=lambda: self.load_view(ProductsView(self.parent), self.products_btn))
        self.home_btn = ctk.CTkButton(
            self.menu_btn_frame,
            text="2", width=40,
            command=lambda: self.load_view(HomeView(self.parent), self.home_btn))
        self.providers_btn = ctk.CTkButton(
            self.menu_btn_frame,
            text="3", width=40,
            command=lambda: self.load_view(ProvidersView(self.parent), self.providers_btn))

        self.products_btn.pack(pady=5)
        self.home_btn.pack(pady=5)
        self.providers_btn.pack(pady=5)
