#...................functions...............
def add(x):
	if x not in tasks:
		tasks.append(x)
		status.append(False)
		print("your task has been successfuly added\n")
	else:
		print(f"{x}: exist!\n")

def display():
	for i, t in enumerate(tasks):
		flag = "undone"
		if status[i]:
			flag = "done"
		print(f"task_{i+1}: {t} ----> {flag}")

def edit(list1):
	for i in list1:
		new_task = input("new task: ")
		if new_task not in tasks:
			tasks[i] = new_task
		else:
			print(f"{new_task}: exist!")

def done(list1):
	for i in list1:
		status[i] = True

def search(word):
	for i, t in enumerate(tasks):
		if word in t:
			flag = "undone"
			if status[i]:
				flag = "done"
			print(f"{t} ----> {flag}")

#...............main...............
tasks = ["hw"] # string
status = [True] # boolean
# add, remove, edit, search
while True:
	user = input("To-Do List>> Select one option(add/edit/remove/search/display) :")
	if user == "add":
		task = input("Enter your task to add: ")
		add(task)
	elif user == "display":
		display()
	elif user == "edit":
		display()
		index = input("index of task: ") # 1 2 3 4
		list1 = [int(i)-1 for i in index.split()]
		edit(list1)
	elif user == "done":
		display()
		index = input("index of task: ") # 1 2 3 4
		list1 = [int(i)-1 for i in index.split()]
		done(list1)
	elif user == "remove":
		"""index = input("index of task: ") # 1 2 3 4
		list1 = [int(i)-1 for i in index.split()]
		for i in list1:
			tasks.pop(i)
			status.pop(i)"""
		pass
	elif user == "search":
		word = input("task to search: ")
		search(word)
	elif user == "":
		pass
	elif user == "exit":
		break
	else:
		print(f"{user}: command not found!")
