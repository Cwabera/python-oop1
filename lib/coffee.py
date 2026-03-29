class Coffee:
    def __init__(self, name, price, size):
        # Validation (very commonly tested)
        if not isinstance(name, str) or name == "":
            raise ValueError("Name must be a non-empty string")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        if size not in ["small", "medium", "large"]:
            raise ValueError("Size must be 'small', 'medium', or 'large'")

        self.name = name
        self.price = float(price)
        self.size = size

    def drink(self):
        return f"You are drinking a {self.size} {self.name}."

    def __str__(self):
        return f"{self.size.capitalize()} {self.name} - ${self.price:.2f}"

    def __repr__(self):
        return f"Coffee('{self.name}', {self.price}, '{self.size}')"