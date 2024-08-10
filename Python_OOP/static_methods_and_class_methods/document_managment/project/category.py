class Category:
    def __init__(self, cat_id: int, name: str) -> None:
        self.id = cat_id
        self.name = name

    def edit(self, new_name: str):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"

