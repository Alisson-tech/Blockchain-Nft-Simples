class Item:
    def __init__(self, name, description, initial_price, owner):
        self.name = name
        self.description = description
        self.initial_price = initial_price
        self.owner = owner

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "initial_price": self.initial_price,
            "owner": self.owner
        }