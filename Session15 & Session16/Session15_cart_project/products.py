class Product:
    def __init__(self, p_id, name, price, number, discount = 0):
        self.p_id = p_id
        self.name = name
        self.number = number
        self.price = price
        self.discount = discount
    def get_name(self):
        print(f"name of product: {self.name}")

    def get_price(self):
        print(f"name of product: {self.price}")

    def total_price(self):
        t_price = self.price * self.number
        print(f"total price: {t_price}")
    
    def get_all_info(self):
        print(f"name of product: {self.name}")
        print(f"p_id of {self.name}: {self.p_id}")
        print(f"number of {self.name}: {self.number}")
        print(f"price of {self.name}: {self.price}")
        print(f"discount of {self.name}: {self.discount}")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    p1 = Product("1", "p1", 10, 2)
    p2 = Product("2", "p2", 100, 2, 4)
    if p1.price > p2.price:
        p1.get_all_info()
    else:
        p2.get_all_info()