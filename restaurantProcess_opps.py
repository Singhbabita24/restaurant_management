# ---------------- RESTAURANT MANAGEMENT SYSTEM ---------------- #

import random


class Restaurant:

    # ---------- CLASS VARIABLES ---------- #

    restaurant_name = "Rose Restaurant"
    location = "Delhi"

    veg_menu = {
        "Idli": 30,
        "Vada": 25,
        "Dosa": 100,
        "Sheera": 25
    }

    non_veg_menu = {
        "Chicken Biryani": 160,
        "Mutton Biryani": 280,
        "Fish Fry": 150,
        "Crab": 300
    }

    snacks_menu = {
        "Tea": 20,
        "Coffee": 50,
        "Poha": 30,
        "Samosa": 25
    }

    # ---------- CONSTRUCTOR ---------- #

    def __init__(self, customer_name, phone_no):

        self.customer_name = customer_name
        self.phone_no = phone_no

        self.bill_no = random.randint(1000, 9999)

        self.total_items = 0
        self.total_bill = 0

    # ---------- DISPLAY MENUS ---------- #

    @classmethod
    def display_veg_menu(cls):

        print("\n----- VEG MENU -----")

        for item, price in cls.veg_menu.items():
            print(f"{item:<20} ₹{price}")

    @classmethod
    def display_non_veg_menu(cls):

        print("\n----- NON-VEG MENU -----")

        for item, price in cls.non_veg_menu.items():
            print(f"{item:<20} ₹{price}")

    @classmethod
    def display_snacks_menu(cls):

        print("\n----- SNACKS MENU -----")

        for item, price in cls.snacks_menu.items():
            print(f"{item:<20} ₹{price}")

    # ---------- ORDER FUNCTION ---------- #

    def order(self, item_name, price, quantity=1):

        total_price = price * quantity

        self.total_bill = self.add(self.total_bill, total_price)

        self.total_items = self.add(self.total_items, quantity)

        print(f"\n{item_name} x {quantity} added successfully")
        print(f"Added Amount : ₹{total_price}")

    # ---------- CANCEL FUNCTION ---------- #

    def cancel(self, item_name, price, quantity=1):

        total_price = price * quantity

        self.total_bill = self.sub(self.total_bill, total_price)

        self.total_items = self.sub(self.total_items, quantity)

        print(f"\n{item_name} x {quantity} cancelled successfully")
        print(f"Reduced Amount : ₹{total_price}")

    # ---------- DISPLAY BILL ---------- #

    def display_bill(self):

        print("\n========== FINAL BILL ==========")

        print(f"Bill Number    : {self.bill_no}")
        print(f"Customer Name  : {self.customer_name}")
        print(f"Phone Number   : {self.phone_no}")

        print(f"Total Items    : {self.total_items}")
        print(f"Total Bill     : ₹{self.total_bill}")

        print("================================")

    # ---------- STATIC METHODS ---------- #

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


# ---------------- MAIN PROGRAM ---------------- #

if __name__ == "__main__":

    # object creation
    customer1 = Restaurant("Babita", 9876543210)

    # display menus
    Restaurant.display_veg_menu()
    Restaurant.display_non_veg_menu()
    Restaurant.display_snacks_menu()

    # placing orders
    customer1.order(
        "Idli",
        Restaurant.veg_menu["Idli"],
        2
    )

    customer1.order(
        "Vada",
        Restaurant.veg_menu["Vada"],
        2
    )

    customer1.order(
        "Coffee",
        Restaurant.snacks_menu["Coffee"],
        1
    )

    # display bill
    customer1.display_bill()

    # cancel order
    customer1.cancel(
        "Idli",
        Restaurant.veg_menu["Idli"],
        1
    )

    # updated bill
    customer1.display_bill()
