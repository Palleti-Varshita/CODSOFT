tasks = []
i=1
while True:
    print("\n===== To-Do List =====")
    print("Welcome to the application !/nHere are your options:-")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice=="1":
        if not tasks:
            print("No tasks added !")
        else:
            for task in tasks:
                status = "*****" if task["completed"] else " "
                print(str(i)+ ". ["+status+"] "+task['task'])
                i+=1
            i = 1
    elif choice == "2":
        taskdes = input("Enter your task into the list:-  ")
        tasks.append({"task": taskdes, "completed": False})
        print("Done there ! Task is added")

    elif choice == "3":
        if not tasks:
            print("Oops..No tasks to complete")
        else:
            for task in tasks:
                status = "*****" if task["completed"] else " "
                print(str(i)+". ["+status+"] "+task['task'])
                i += 1
            i = 1
            taskind = input("Enter task number to complete: ")
            if taskind.isdigit():
                index = int(taskind) - 1
                if 0<=index<len(tasks):
                    tasks[index]["completed"]=True
                    print("Your task is now marked as completed.. Good job")
                else:
                    print("Invalid task number.. Check again")
            else:
                print("Yikes..Invalid input, please enter a number")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete")
        else:
            for task in tasks:
                status = "*****" if task["completed"] else " "
                print(str(i) + ". [" + status + "] " + task['task'])
                i += 1
            i = 1
            taskind = input("Enter task number to delete: ")
            if taskind.isdigit():
                index=int(taskind) - 1
                if 0<=index<len(tasks):
                    del tasks[index]
                    print("Task deleted.")
                else:
                    print("Invalid task number.. Check again")
            else:
                print("Yikes..Invalid input, please enter a number")

    elif choice == "5":
        print("Thank you for using.. /n We are now exiting the program.")
        break

    else:
        print("Invalid choic,  Please enter a number from 1 to 5 given..")
