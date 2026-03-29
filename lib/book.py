class Book:
    def __init__(self, title, author, pages):
        # Basic validation (tests often expect this)
        if not isinstance(title, str) or title == "":
            raise ValueError("Title must be a non-empty string")
        if not isinstance(author, str) or author == "":
            raise ValueError("Author must be a non-empty string")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Pages must be a positive integer")

        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        return f"You are reading '{self.title}' by {self.author}."

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"