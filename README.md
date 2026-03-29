# 📚☕ Bookstore OOP Lab

## 📖 Overview

This project models a simple bookstore using Object-Oriented Programming (OOP) in Python. It includes two main classes:

* **Book** → Represents a book in the store
* **Coffee** → Represents a coffee item sold in the store

The goal of this lab is to practice:

* Class creation
* Attribute validation using property setters
* Method implementation
* Matching strict test expectations (including printed output)

---

## 📂 Project Structure

```
PYTHON-OOP1/
│
├── lib/
│   ├── book.py
│   ├── coffee.py
│   └── testing/
│       ├── book_test.py
│       ├── coffee_test.py
│       └── conftest.py
│
├── Pipfile
├── pytest.ini
└── README.md
```

---

## 📚 Book Class

### Features

* Stores:

  * `title` (string)
  * `page_count` (integer)
* Validates that `page_count` is an integer
* Uses a **property setter** for validation
* Includes a method to simulate turning a page

### Behavior

```python
book = Book("Python Basics", 100)
book.turn_page()
```

Output:

```
Flipping the page...wow, you read fast!
```

If invalid page count:

```
page_count must be an integer
```

---

## ☕ Coffee Class

### Features

* Stores:

  * `size` (must be: Small, Medium, Large)
  * `price` (numeric)
* Uses a **property setter** for size validation
* Includes a `tip()` method

### Behavior

```python
coffee = Coffee("Small", 3.5)
coffee.tip()
```

Output:

```
This coffee is great, here’s a tip!
```

If invalid size:

```
size must be Small, Medium, or Large
```

---

## ⚙️ Setup Instructions

### 1. Install dependencies

```bash
pipenv install
```

### 2. Activate virtual environment

```bash
pipenv shell
```

---

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest lib/testing/book_test.py
```

---

## ⚠️ Important Notes

* Validation messages must match **exactly** (including capitalization and punctuation)
* The `tip()` method prints output and updates price
* The `turn_page()` method prints output (does not return a string)
* Property setters are used to enforce validation after initialization

---

## 🧠 Concepts Covered

* Python classes and objects
* Constructors (`__init__`)
* Property decorators (`@property`, `@setter`)
* Input validation
* Unit testing with pytest
* Debugging based on test feedback

---

## ✅ Status

✔ All tests passing
✔ Fully compliant with lab requirements

---

## 🚀 Next Steps (Optional Improvements)

* Add inventory tracking
* Add multiple coffee types (latte, espresso, etc.)
* Add reading progress tracking for books
* Build a CLI or simple UI for interaction

---

## 👨‍💻 Author

Charles Ngatia
