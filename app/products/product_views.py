import customtkinter as ctk
from config import TITLE_FONT


class ProductsView(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent)
        self.parent = parent
        self.pack_propagate(False)

        self.search_bar = SearchBar(self)
        self.products_cards_frame = ProductsCardsFrame(self)
        self.product_info_frame = ProductInfoFrame(self)

    def show(self) -> None:
        self.pack(fill="both", expand=True, side="left")

    def remove(self) -> None:
        self.pack_forget()


class SearchBar(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, height=50)
        self.pack_propagate(False)

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.searchbar = ctk.CTkEntry(self.container, width=400)
        self.search_btn = ctk.CTkButton(self.container, text="Buscar")

        self.searchbar.pack(side="left", padx=5)
        self.search_btn.pack(side="left", padx=5)
        self.container.pack(expand=True)
        self.pack(fill="x")


class ProductsCardsFrame(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent)
        self.pack_propagate(False)

        self.title = ctk.CTkLabel(
            self, text="Últimos Productos", font=TITLE_FONT)

        self.title.pack(pady=5)
        self.pack(side="left", expand=True, fill="both")


class ProductInfoFrame(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent)
        self.pack_propagate(False)

        self.title = ctk.CTkLabel(
            self, text="Información Detallada", font=TITLE_FONT)

        self.title.pack(pady=5)
        self.pack(side="left", expand=True, fill="both")


class ProductCard(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, fg_color="#4f61dd")
        self.pack_propagate(False)
        # TODO: Implementar

        self.pack()
