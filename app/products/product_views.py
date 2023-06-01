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
        # TODO: Remove Test
        ProductCard(self)
        ProductCard(self)
        ProductCard(self)
        ProductCard(self)
        ProductCard(self)
        ProductCard(self)
        ProductCard(self)

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
        super().__init__(
            master=parent, fg_color="#4f61dd", border_width=2,
            border_color="orange", corner_radius=10)
        self.pack_propagate(False)

        self.columnconfigure(0, weight=7, uniform="a")
        self.columnconfigure(1, weight=4, uniform="a")
        self.columnconfigure(2, weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=1, uniform="a")

        self.name = ctk.CTkLabel(
            self, text="Titulo provisorio algo largo x si aca a ver",
            font=("Roboto", 18))
        self.category = ctk.CTkLabel(
            self, text="Camisetas",
            fg_color="transparent", font=("Roboto", 16))
        self.price = ctk.CTkLabel(self, text="29.99€")
        self.info_btn = ctk.CTkButton(self, text="->", fg_color="orange")

        self.name.grid(column=0, row=0, rowspan=2)
        self.category.grid(column=1, row=0, sticky="e", padx=5)
        self.price.grid(column=1, row=1, sticky="e", padx=5, pady=5)
        self.info_btn.grid(column=2, row=0, rowspan=2, sticky="nswe")

        self.pack(fill="x", padx=5, pady=3)
