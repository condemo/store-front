import requests
from tkinter.messagebox import showerror

from config import ROOT_DIR


class DataLoadCache:
    # TODO: Fetchea los datos necesatios.
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

    # TODO: Crea un JSON con los datos estructurados.
    def to_json(self) -> None:
        with open(ROOT_DIR + "/data/data.json", "w") as file:
            # TODO: Implenetar la funcion para crear un json estructurado
            pass

    # TODO: Divide los datos en distintos diccionarios que se cargan en las vistas.
