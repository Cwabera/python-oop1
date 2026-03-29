class Coffee:
    def __init__(self, price, size):
        self.price = price

        allowed_sizes = ["small", "medium", "large"]

        if size in allowed_sizes:
            self.size = size
        else:
            print("size must be small, medium, or large")

    def tip(self, amount):
        self.price += amount