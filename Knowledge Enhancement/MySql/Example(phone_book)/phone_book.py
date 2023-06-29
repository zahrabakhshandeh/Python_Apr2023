from functions import *
while True:
    answer = input("add/remove/search/exit: ")
    if answer == "add":
        name = input("name of your contact: ")
        phone = input(f"{name}'s phone: ")
        add(name, phone)
    elif answer == "search":
        name = input("name of your contact: ")
        results = search(name)
        for id_, name, phone in results:
            print(f"{id_}: {name} ---> {phone}")
    elif answer == "remove":
        name = input("name of your contact: ")
        delete(name)
    elif answer == "":
        pass
    elif answer == "exit":
        break
    else:
        print(f"{answer}: cammand not found!")