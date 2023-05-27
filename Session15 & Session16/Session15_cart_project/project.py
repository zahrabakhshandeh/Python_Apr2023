from products import *
from cart import *

if __name__ == "__main__":
    # create a cart
    cart1 = Cart()

    while True:
        user = input("Please select an option: add/remove/edit/search/exit: ")
        user = user.lower()
        if user == "add":
            product_info = input("enter info of your product: ")
            info = product_info.split()
            p1 = Product(info[0], info[1], int(info[2]), int(info[3]), int(info[4]))
            cart1.add_product(p1)
        elif user == "remove":
            id = input("enter a id to remove: ")
            cart1.remove(id)
        elif user == "edit":
            id = input("enter a id to edit: ")
            cart1.edit(id)
        elif user == "search":
            #p1 = Product("1", "p1", 10, 2, 1)
            id = input("enter a id to search: ")
            cart1.search(id)
        elif user == "display":
            cart1.display()
        elif user == "":
            pass
        elif user == "exit":
            break
        else:
            print(f"{user}: command not found!")