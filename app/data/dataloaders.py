from config import ROOT_DIR
import json


class ProductLoader:
    def __init__(self) -> None:
        self.products: list
        with open(ROOT_DIR + "/data/data.json") as file:
            data = json.load(file)

        self.products = data["products"]
        del data
        # TODO: Implementar
