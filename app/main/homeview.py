import customtkinter as ctk


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


class TopHomeFrame(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent)
        self.pack_propagate(False)

        self.last_movement_frame = LastMovements(self)
        self.next_order_frame = NextOrders(self)

        self.last_movement_frame.pack(side="left", expand=True, fill="both")
        self.next_order_frame.pack(side="left", expand=True, fill="both")

        self.pack(expand=True, fill="both")


class LastMovements(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, fg_color="red")
        self.pack_propagate(False)
        self.title = ctk.CTkLabel(self, text="Últimos Movimientos", font=("Roboto", 20))

        self.title.pack(pady=5)


class NextOrders(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, fg_color="blue")
        self.pack_propagate(False)
        self.title = ctk.CTkLabel(self, text="Próximos Pedidos", font=("Roboto", 20))

        self.title.pack(pady=5)


class BottomHomeView(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, fg_color="orange")
        self.pack_propagate(False)

        self.pack(expand=True, fill="both")
