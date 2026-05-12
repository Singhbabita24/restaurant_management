# 🍽️ Restaurant Management System — OOP in Python

A Python-based Restaurant Management System that simulates menu display, order placement, order cancellation, and bill generation using **Object-Oriented Programming** principles.

---

## 📁 File

```
restaurantProcess_opps.py
```

---

## 🧠 Concepts Covered

| Concept | Implementation |
|---|---|
| **Class & Object** | `Restaurant` class with customer instances |
| **Class Variables** | Shared menus and restaurant info |
| **Instance Variables** | Customer name, phone, bill number, totals |
| **Class Methods** | Menu display methods |
| **Static Methods** | `add()`, `sub()` utility methods |
| **Constructor** | `__init__` with random bill number generation |
| **Encapsulation** | All billing logic contained within the class |

---

## 🗂️ Class Structure

```
Restaurant
  ├── Class Variables
  │     ├── restaurant_name, location
  │     ├── veg_menu      { item: price }
  │     ├── non_veg_menu  { item: price }
  │     └── snacks_menu   { item: price }
  │
  ├── Instance Variables
  │     ├── customer_name, phone_no
  │     ├── bill_no (random 4-digit)
  │     ├── total_items
  │     └── total_bill
  │
  ├── display_veg_menu()      [classmethod]
  ├── display_non_veg_menu()  [classmethod]
  ├── display_snacks_menu()   [classmethod]
  ├── order(item, price, qty)
  ├── cancel(item, price, qty)
  ├── display_bill()
  ├── add(a, b)               [staticmethod]
  └── sub(a, b)               [staticmethod]
```

---

## 🍴 Menu

### 🥦 Veg Menu
| Item | Price |
|---|---|
| Idli | ₹30 |
| Vada | ₹25 |
| Dosa | ₹100 |
| Sheera | ₹25 |

### 🍗 Non-Veg Menu
| Item | Price |
|---|---|
| Chicken Biryani | ₹160 |
| Mutton Biryani | ₹280 |
| Fish Fry | ₹150 |
| Crab | ₹300 |

### ☕ Snacks Menu
| Item | Price |
|---|---|
| Tea | ₹20 |
| Coffee | ₹50 |
| Poha | ₹30 |
| Samosa | ₹25 |

---

## ▶️ How to Run

```bash
python restaurantProcess_opps.py
```

---

## 💡 Sample Output

```
----- VEG MENU -----
Idli                 ₹30
Vada                 ₹25
...

Idli x 2 added successfully
Added Amount : ₹60

Vada x 2 added successfully
Added Amount : ₹50

Coffee x 1 added successfully
Added Amount : ₹50

========== FINAL BILL ==========
Bill Number    : 4821
Customer Name  : Babita
Phone Number   : 9876543210
Total Items    : 5
Total Bill     : ₹160
================================

Idli x 1 cancelled successfully
Reduced Amount : ₹30

========== FINAL BILL ==========
Bill Number    : 4821
Customer Name  : Babita
Phone Number   : 9876543210
Total Items    : 4
Total Bill     : ₹130
================================
```

---

## 🛒 Ordering Items

Use the `order()` method to add items. Price is fetched directly from the class-level menu dictionaries:

```python
customer1.order("Dosa", Restaurant.veg_menu["Dosa"], 1)
```

---

## ❌ Cancelling Items

Use the `cancel()` method to remove items and reduce the bill:

```python
customer1.cancel("Idli", Restaurant.veg_menu["Idli"], 1)
```

---

## 🎲 Auto Bill Number

Each customer gets a unique **random 4-digit bill number** generated at the time of object creation using Python's `random` module:

```python
self.bill_no = random.randint(1000, 9999)
```

---

## 🛠️ Requirements

- Python 3.x
- Standard library only (`random` module — built-in)

---

## 📌 Use Case

This project is great for understanding how class variables (shared data like menus) and instance variables (per-customer data like bill and orders) work together in a real-world OOP scenario.
