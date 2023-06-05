import customtkinter as ctk
from datetime import datetime
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
        super().__init__(master=parent, fg_color="transparent")
        self.pack_propagate(False)
        self.product = product
        self.product_values_list = []
        self.value_color = "yellow"
        self.text_size = 16

        # TODO: Checkear como reestructurar para Implementar mejor
        self.data_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.img_frame = ctk.CTkFrame(self, fg_color="transparent")

        # Two Container Frames
        self.key_frame = ctk.CTkFrame(self.data_frame, fg_color="transparent")
        self.value_frame = ctk.CTkFrame(self.data_frame, fg_color="transparent")

        self.load_key_values()
        self.set_data()
        self.show_data()

        self.key_frame.pack(side="left", fill="both", expand=True)
        self.value_frame.pack(side="left", expand=True, fill="both")
        self.data_frame.pack(expand=True, fill="both")
        self.img_frame.pack(expand=True, fill="both")
        self.pack(expand=True, fill="both", pady=10)

    def load_key_values(self) -> None:
        self.name_label = ctk.CTkLabel(
            self.key_frame, text="Nombre: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        self.brand_label = ctk.CTkLabel(
            self.key_frame, text="Marca: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        self.category_label = ctk.CTkLabel(
            self.key_frame, text="Categoria: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        self.price_label = ctk.CTkLabel(
            self.key_frame, text="Precio: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        self.provider_price_label = ctk.CTkLabel(
            self.key_frame, text="Precio Proveedor: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        self.stock_label = ctk.CTkLabel(
            self.key_frame, text="Stock: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        self.discount_label = ctk.CTkLabel(
            self.key_frame, text="Descuento: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        self.discount_status_label = ctk.CTkLabel(
            self.key_frame, text="Desc Status: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        self.uuid_label = ctk.CTkLabel(
            self.key_frame, text="UUID: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        self.created_at_label = ctk.CTkLabel(
            self.key_frame, text="Fecha de Creación: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        self.updated_at_label = ctk.CTkLabel(
            self.key_frame, text="Última actualización: ",
            anchor="e", text_color=self.value_color, font=("Roboto", self.text_size))
        #
        self.name_label.pack(fill="x")
        self.brand_label.pack(fill="x")
        self.category_label.pack(fill="x")
        self.price_label.pack(fill="x")
        self.provider_price_label.pack(fill="x")
        self.stock_label.pack(fill="x")
        self.discount_label.pack(fill="x")
        self.discount_status_label.pack(fill="x")
        self.uuid_label.pack(fill="x")
        self.created_at_label.pack(fill="x")
        self.updated_at_label.pack(fill="x")

    def set_data(self) -> None:
        # TODO: Implementar mejor, muchas lineas
        self.name = ctk.CTkLabel(
            self.value_frame, text=f"{self.product.name}",
            anchor="w", font=("Roboto", self.text_size))
        self.brand = ctk.CTkLabel(
            self.value_frame, text=f"{self.product.brand['name']}",
            anchor="w", font=("Roboto", self.text_size))
        self.category = ctk.CTkLabel(
            self.value_frame, text=f"{self.product.category['name']}",
            anchor="w", font=("Roboto", self.text_size))
        self.price = ctk.CTkLabel(
            self.value_frame, text=f"{str(self.product.price)}€",
            anchor="w", font=("Roboto", self.text_size))
        self.provider_price = ctk.CTkLabel(
            self.value_frame, text=f"{str(self.product.provider_price)}€",
            anchor="w", font=("Roboto", self.text_size))
        self.stock = ctk.CTkLabel(
            self.value_frame, text=f"{self.product.stock['qty']} unidades",
            anchor="w", font=("Roboto", self.text_size))
        if self.product.discount:
            self.discount = ctk.CTkLabel(
                self.value_frame, text=f"{self.product.discount['discount_percent']}%",
                anchor="w", font=("Roboto", self.text_size))
            self.discount_status = ctk.CTkLabel(
                self.value_frame, text=f"{self.product.discount['active']}",
                anchor="w", font=("Roboto", self.text_size))
        else:
            self.discount = ctk.CTkLabel(self.value_frame, text="No asigado",
                                         anchor="w", font=("Roboto", self.text_size))
            self.discount_status = ctk.CTkLabel(self.value_frame, text="",
                                                anchor="w", font=("Roboto", self.text_size))
        self.uuid = ctk.CTkLabel(self.value_frame, text=f"{self.product.uuid}",
                                 anchor="w", font=("Roboto", self.text_size))
        self.created_at = ctk.CTkLabel(
            self.value_frame, text=f"{self.product.created_at}",
            anchor="w", font=("Roboto", self.text_size))
        if self.product.updated_at:
            self.updated_at = ctk.CTkLabel(
                self.value_frame, text=f"{self.product.updated_at}",
                anchor="w", font=("Roboto", self.text_size))
        else:
            self.updated_at = ctk.CTkLabel(self.value_frame, text="Nunca",
                                           anchor="w", font=("Roboto", self.text_size))

        self.product_values_list.append(self.name)
        self.product_values_list.append(self.brand)
        self.product_values_list.append(self.category)
        self.product_values_list.append(self.price)
        self.product_values_list.append(self.provider_price)
        self.product_values_list.append(self.stock)
        self.product_values_list.append(self.discount)
        self.product_values_list.append(self.discount_status)
        self.product_values_list.append(self.uuid)
        self.product_values_list.append(self.created_at)
        self.product_values_list.append(self.updated_at)

    def show_data(self) -> None:
        [i.pack(fill="x") for i in self.product_values_list]
