tasks = ["hw"] # string
status = [True] # boolean
# add, remove, edit, search
while True:
	user = input("To-Do List>> Select one option(add/edit/remove/search/display) :")
	if user == "add":
		task = input("Enter your task to add: ")
		if task not in tasks:
			tasks.append(task)
			status.append(False)
			print("your task has been successfuly added\n")
		else:
			print(f"{task}: exist!\n")
	elif user == "display":
		for i, t in enumerate(tasks):
			# task_1 = python ----> done
			# True ===> done, False ===> undone
			flag = "undone"
			if status[i]:
				flag = "done"
			print(f"task_{i+1}: {t} ----> {flag}")
	elif user == "edit":
		index = input("index of task: ") # 1 2 3 4
		list1 = [int(i)-1 for i in index.split()]
		for i in list1:
			new_task = input("new task: ")
			if new_task not in tasks:
				tasks[i] = new_task
			else:
				print(f"{new_task}: exist!")
	elif user == "done":
		index = input("index of task: ") # 1 2 3 4
		list1 = [int(i)-1 for i in index.split()]
		for i in list1:
			status[i] = True
	elif user == "remove":
		index = input("index of task: ") # 1 2 3 4
		list1 = [int(i)-1 for i in index.split()]
		for i in list1:
			tasks.pop(i)
			status.pop(i)
	elif user == "search":
		word = input("task to search: ")
		for i, t in enumerate(tasks):
			if word in t:
				flag = "undone"
				if status[i]:
					flag = "done"
				print(f"{t} ----> {flag}")
	elif user == "":
		pass
	elif user == "exit":
		break
	else:
		print(f"{user}: command not found!")
