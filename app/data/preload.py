import json
import requests
from tkinter.messagebox import showerror

from config import ROOT_DIR


class DataLoadCache:
    def __init__(self, url: str) -> None:
        self.products_data = []
        self.discounts_data = []
        self.orders_data = []
        self.providers_data = []

        try:
            self.products_data = requests.get(
                f"{url}/products/?limit=10").json()
            self.discounts_data = requests.get(
                f"{url}/products/discounts/?limit=10").json()
            self.orders_data = requests.get(
                f"{url}/providers/orders/?limit=10").json()
            self.providers_data = requests.get(
                f"{url}/providers/?limit=10").json()

        except requests.exceptions.ConnectionError:
            showerror(
                title="Error de conexión",
                message="Imposible comunicarse con el servidor"
            )
            exit()

        self.to_json()

    def to_json(self) -> None:
        with open(ROOT_DIR + "/data/data.json", "w") as file:
            new_json = {
                "products": self.products_data,
                "discounts": self.discounts_data,
                "orders": self.orders_data,
                "providers": self.providers_data,
            }
            json.dump(new_json, file, indent=4)
