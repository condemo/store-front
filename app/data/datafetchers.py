import requests

from config import DATA_URL
from products import ProductFull


def product_info_loader(id: int) -> ProductFull:
    product = requests.get(f"{DATA_URL}/products/{id}").json()
    return ProductFull(**product)
