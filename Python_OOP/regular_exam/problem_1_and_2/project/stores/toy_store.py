from collections import defaultdict

from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, 100)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        model_count = defaultdict(list)
        for product in self.products:
            model_count[product.model].append(product.price)

        details = []
        for model, prices in sorted(model_count.items()):
            avg_price = sum(prices) / len(prices)
            details.append(f"{model}: {len(prices)}pcs, average price: {avg_price:.2f}")

        return (
                f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}\n"
                f"{self.get_estimated_profit()}\n"
                f"**Toys for sale:\n"
                + "\n".join(details)
        )

