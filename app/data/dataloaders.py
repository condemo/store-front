from config import ROOT_DIR
import json

from products import ProductMin


# TODO: Renombrar este clase mejor ya que devuelve una lista de 10 productos para las tarjetas
class ProductCardLoader:
    def __init__(self) -> None:
        self.products: list[ProductMin]

        with open(ROOT_DIR + "/data/data.json") as file:
            data = json.load(file)

        raw_product_data = data["products"]
        del data

        self.products = [ProductMin(
            id=i["id"],
            name=i["name"],
            category=i["category"]["name"],
            price=i["price"]
        ) for i in raw_product_data]

    def get_data_list(self) -> list[ProductMin]:
        return self.products
