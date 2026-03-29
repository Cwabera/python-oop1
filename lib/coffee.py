class Coffee:
    def __init__(self, size, price):
        self.price = price
        self._size = None
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        self.price += 1