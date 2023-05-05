# name of products
products = []
# price of products
prices = []
while True:
    user = input("""Please Enter a Option\
    (add/edit/remove/display/search/detail/exit): """)
    if user == "add":
        num = int(input("Please Enter number of Products to add: "))
        for i in range(num):
            name = input(f"name of product_{i+1}: ")
            if name not in products:
                price = int(input(f"price of {name}: "))
                products.append(name)
                prices.append(price)
            else:
                print(f"{name}: exist!")
    elif user == "edit":
        names = input("names of products to edit: ")
        # p1 p2 p3
        names = names.split() # ["p1", "p2", "p3"]
        for name in names:
            if name in products:
                i = products.index(name)
                prices[i] = int(input(f"new price of {name}: "))
            else:
                print(f"{name}: not found!")

    elif user == "remove":
        names = input("names of products to remove: ")
        # p1 p2 p3
        names = names.split() # ["p1", "p2", "p3"]
        for name in names:
            if name in products:
                i = products.index(name)
                products.pop(i)
                prices.pop(i)
            else:
                print(f"{name}: not found!")

    elif user == "display":
        for i, product in enumerate(products):
            print(f"product_{i+1}: {product} --> {prices[i]}")
    elif user == "search":
        name = input("name of product to search: ")
        if name in products:
            i = products.index(name)
            print(f"{name} ---> {prices[i]}")
        else:
            print(f"{name}: not found!")
    elif user == "detail":
        l = len(prices)
        avg = sum(prices) / l
        max1 = max(prices)
        min1 = min(prices)
        i_max = prices.index(max1)
        i_min = prices.index(min1)
        max_product = products[i_max]
        min_product = products[i_min]
        print(f"number of products: {l}")
        print(f"avg of prices: {avg}")
        print(f"max: {max_product} --> {max1}")
        print(f"min: {min_product} --> {min1}")
    elif user == "":
        pass
    elif user == "exit":
        break
    else:
        print(f"{user}: command not found!")