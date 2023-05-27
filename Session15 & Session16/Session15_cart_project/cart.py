from products import *
class Cart:
    def __init__(self):
        self.products = []
    
    def find_index(self, id):
        for i, item in enumerate(self.products):
            if item.p_id == id:
                return i
        return -1
    
    def add_product(self, product):
        index = self.find_index(product.p_id)
        if index == -1:
            self.products.append(product)
            print("added")
        else:
            print(f"Product with p_id = {product.p_id} exist")
    
    def display(self):
        l = len(self.products)
        if l == 0:
            print("Empty")
            return
        for p in self.products:
            Product.get_all_info(p)
    
    def search(self, id):
        # obj ====> a product
        index = self.find_index(id)
        if index != -1:
            self.products[index].get_all_info()
        else:
            print("not found!")
    
    def edit(self, id):
        index = self.find_index(id)
        if index != -1:
            new_info = input("name,price,number,discount: ")
            info = new_info.split(",")
            self.products[index].name = info[0] or self.products[index].name
            self.products[index].price = info[1] or self.products[index].price
            self.products[index].price = int(self.products[index].price)
            self.products[index].number = info[2] or self.products[index].number
            self.products[index].number = int(self.products[index].number)
            self.products[index].discount = info[3] or self.products[index].discount
            self.products[index].discount = int(self.products[index].discount)
            print("edited")
        else:
            print("not found!")

    def remove(self, id):
        index = self.find_index(id)
        if index != -1:
            self.products.pop(index)
            print("remove")
        else:
            print("not found!")

if __name__ == "__main__":
    c1 = Cart()
    print(c1.products)