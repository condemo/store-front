import customtkinter as ctk


class ProductsView(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent)
        self.parent = parent
        self.pack_propagate(False)

        self.search_bar = SearchBar(self)

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
