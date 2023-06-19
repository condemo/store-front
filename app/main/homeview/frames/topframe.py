import customtkinter as ctk
from lib.cards import EventCard


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
        self.container = ctk.CTkFrame(self)

        self.title.pack(pady=5)
        self.test_card = LastMovementsCard(self.container)
        self.container.pack(expand=True, fill="both")


class LastMovementsCard(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(
            master=parent, height=80, border_width=3,
            border_color="red", corner_radius=10,
        )
        self.pack_propagate(False)
        self.parent = parent

        # TODO: Hardcoded, implementar
        self.data: EventCard = {
            "event_type": "test",
            "text": "a ver que onda",
            "date": "2023-06-19 23:37"
            }
        self.type = ctk.CTkLabel(self, text=f"{self.data['event_type']}", font=("Roboto", 18))
        self.text = ctk.CTkLabel(self, text=f"{self.data['text']}")
        self.date = ctk.CTkLabel(self, text=f"{self.data['date']}")

        self.type.pack(pady=3)
        self.text.pack()
        self.date.pack(pady=3)
        self.pack(fill="both", padx=5, pady=3, ipady=5)


class NextOrders(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(master=parent, fg_color="blue")
        self.pack_propagate(False)
        self.title = ctk.CTkLabel(self, text="Próximos Pedidos", font=("Roboto", 20))
        self.container = ctk.CTkFrame(self)

        self.title.pack(pady=5)
        self.test_card = NextOrdersCard(self.container)
        self.container.pack(expand=True, fill="both")


class NextOrdersCard(ctk.CTkFrame):
    def __init__(self, parent) -> None:
        super().__init__(
            master=parent, height=80, border_width=3,
            border_color="blue", corner_radius=10,
        )
        self.pack_propagate(False)

        self.arrive_date = ctk.CTkLabel(self, text="2023-06-20", font=("Roboto", 18))
        self.product_count = ctk.CTkLabel(self, text=f"{str(14)} productos")
        self.provider = ctk.CTkLabel(self, text="Empresa S.A.")

        self.arrive_date.pack(pady=3)
        self.product_count.pack()
        self.provider.pack(pady=3)
        self.pack(fill="both", padx=5, pady=3, ipady=5)
