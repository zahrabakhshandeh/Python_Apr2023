def user_input(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print("Invalid input, please enter an integer")