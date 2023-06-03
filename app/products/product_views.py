import customtkinter as ctk
from config import TITLE_FONT
from data.dataloaders import ProductCardLoader
from data.datafetchers import product_info_loader
from products import ProductFull


class ProductsView(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent)
        self.parent = parent
        self.pack_propagate(False)

        self.search_bar = SearchBar(self)
        self.products_cards_frame = ProductsCardsFrame(self)

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
        self.parent = parent

        self.title = ctk.CTkLabel(
            self, text="Últimos Productos", font=TITLE_FONT)

        self.title.pack(pady=5)
        self.load_product_cards()

        self.pack(side="left", expand=True, fill="both")
        self.product_info_frame = ProductInfoFrame(self.parent)

    def load_product_cards(self) -> None:
        self.card_loader = ProductCardLoader()
        [ProductCard(
            self,
            id=i.id,
            name=i.name,
            category=i.category,
            price=i.price,
        ) for i in self.card_loader.get_data_list()]

    def load_product_detail(self, product: ProductFull) -> None:
        self.product_info_frame.load_data(product)


class ProductInfoFrame(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent)
        self.pack_propagate(False)

        self.title = ctk.CTkLabel(
            self, text="Información Detallada", font=TITLE_FONT)

        self.title.pack(pady=5)
        self.data_frame = None
        self.pack(side="left", expand=True, fill="both")

    def load_data(self, product) -> None:
        if self.data_frame:
            self.data_frame.pack_forget()
        self.data_frame = ProductDataFrame(self, product)


class ProductCard(ctk.CTkFrame):
    def __init__(self, parent, id: int, name: str, category: str, price: float) -> None:
        super().__init__(
            master=parent, fg_color="#4f61dd", border_width=2,
            border_color="orange", corner_radius=10)
        self.pack_propagate(False)
        self.parent = parent

        self.columnconfigure(0, weight=7, uniform="a")
        self.columnconfigure(1, weight=4, uniform="a")
        self.columnconfigure(2, weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")
        self.rowconfigure(1, weight=1, uniform="a")

        self.id = id

        self.name = ctk.CTkLabel(
            self, text=f"{name}",
            font=("Roboto", 18))
        self.category = ctk.CTkLabel(
            self, text=f"{category}",
            fg_color="transparent", font=("Roboto", 16))
        self.price = ctk.CTkLabel(self, text=f"{str(price)}€")
        self.info_btn = ctk.CTkButton(
            self, text="->", fg_color="orange", command=self.more_info)

        self.name.grid(column=0, row=0, rowspan=2)
        self.category.grid(column=1, row=0, sticky="e", padx=5)
        self.price.grid(column=1, row=1, sticky="e", padx=5, pady=5)
        self.info_btn.grid(column=2, row=0, rowspan=2, sticky="nswe")

        self.pack(fill="x", padx=5, pady=3)

    def more_info(self) -> None:
        product = product_info_loader(self.id)
        self.parent.load_product_detail(product)


class ProductDataFrame(ctk.CTkFrame):
    def __init__(self, parent, product: ProductFull) -> None:
        super().__init__(master=parent)
        self.pack_propagate(False)
        self.label_list = []

        # TODO: Implementar mejor esta parte el algún momento
        self.name = ctk.CTkLabel(self, text=f"{product.name}")
        self.brand = ctk.CTkLabel(self, text=f"{product.brand['name']}")
        self.category = ctk.CTkLabel(self, text=f"{product.category['name']}")
        self.price = ctk.CTkLabel(self, text=f"{str(product.price)}€")
        self.provider_price = ctk.CTkLabel(self, text=f"{str(product.provider_price)}€")
        self.stock = ctk.CTkLabel(self, text=f"{product.stock['qty']} unidades")
        if product.discount:
            self.discount = ctk.CTkLabel(self, text=f"{product.discount['discount_percent']}%")
            self.discount_status = ctk.CTkLabel(self, text=f"{product.discount['active']}")
        else:
            self.discount = ctk.CTkLabel(self, text="No asigado")
            self.discount_status = ctk.CTkLabel(self, text="")
        self.uuid = ctk.CTkLabel(self, text=f"{product.uuid}")
        self.created_at = ctk.CTkLabel(self, text=f"{product.created_at}")
        if product.updated_at:
            self.updated_at = ctk.CTkLabel(self, text=f"{product.updated_at}")
        else:
            self.updated_at = ctk.CTkLabel(self, text="Nunca")

        self.label_list.append(self.name)
        self.label_list.append(self.brand)
        self.label_list.append(self.category)
        self.label_list.append(self.price)
        self.label_list.append(self.provider_price)
        self.label_list.append(self.stock)
        self.label_list.append(self.discount)
        self.label_list.append(self.discount_status)
        self.label_list.append(self.uuid)
        self.label_list.append(self.created_at)
        self.label_list.append(self.updated_at)

        self.load_data()
        self.pack(expand=True, fill="both")

    def load_data(self) -> None:
        [i.pack() for i in self.label_list]
