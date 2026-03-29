class Coffee:
    def __init__(self, size, price):
        allowed_sizes = ["small", "medium", "large"]

        if size not in allowed_sizes:
            raise Exception("size must be small, medium, or large")

        self.size = size
        self.price = price

    def tip(self, amount):
        self.price += amount
        return self.price