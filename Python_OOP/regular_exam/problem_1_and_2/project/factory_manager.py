from collections import defaultdict
from typing import List

from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    VALID_PRODUCT_TYPES = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    VALID_STORE_TYPES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products: List[BaseProduct] = []
        self.stores: List[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        if self.VALID_PRODUCT_TYPES.get(product_type):
            product = self.VALID_PRODUCT_TYPES[product_type](model, price)
            self.products.append(product)
            return f"A product of sub-type {product.sub_type} was produced."
        raise Exception("Invalid product type!")

    def register_new_store(self, store_type: str, name: str, location: str):
        if self.VALID_STORE_TYPES.get(store_type):
            store = self.VALID_STORE_TYPES[store_type](name, location)
            self.stores.append(store)
            return f"A new {store_type} was successfully registered."
        raise Exception(f"{store_type} is an invalid type of store!")

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        purchased_products = []
        for product in products:
            if product.sub_type == store.store_type.replace("Store", ""):
                store.products.append(product)
                self.products.remove(product)
                store.capacity -= 1
                purchased_products.append(product.price)

        if purchased_products:
            self.income += sum(purchased_products)
            return f"Store {store.name} successfully purchased {len(purchased_products)} items."
        else:
            return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        for store in self.stores:
            if store.name == store_name:
                if store.products:
                    return "The store is still having products in stock! Unregistering is inadvisable."
                self.stores.remove(store)
                return f"Successfully unregistered store {store_name}, location: {store.location}."
        raise Exception("No such store!")

    def discount_products(self, product_model: str):
        discounted_count = 0
        for product in self.products:
            if product.model == product_model:
                product.discount()
                discounted_count += 1
        return f"Discount applied to {discounted_count} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        for store in self.stores:
            if store.name == store_name:
                return store.store_stats()
        return "There is no store registered under this name!"

    def statistics(self):
        products_by_model = defaultdict(int)
        total_price = 0.0

        for product in self.products:
            products_by_model[product.model] += 1
            total_price += product.price

        store_names = sorted(store.name for store in self.stores)
        product_models = sorted(products_by_model.items())

        return (
                f"Factory: {self.name}\n"
                f"Income: {self.income:.2f}\n"
                f"***Products Statistics***\n"
                f"Unsold Products: {len(self.products)}. Total net price: {total_price:.2f}\n"
                + "\n".join(f"{model}: {count}" for model, count in product_models) + "\n"
                f"***Partner Stores: {len(self.stores)}***\n"
                + "\n".join(store_names)
        )




