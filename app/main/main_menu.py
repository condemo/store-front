import customtkinter as ctk

from utils import ViewController
from products import ProductsView
from lib import View


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
        pass

    def load_buttons(self) -> None:
        # TODO: Implementar los botones aquí
        [ctk.CTkButton(
            self.menu_btn_frame, text=f"{i+1}", width=40)
            .pack(pady=5) for i in range(5)]
