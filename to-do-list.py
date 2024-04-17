class to_do_list:
    def __init__(self):
        self.lst = []
    
    def add(self, task):
        self.lst.append(task)
        return "Task added successfully."
    
    def remove(self, task):
        try:
            self.lst.remove(task)
            return "Task removed successfully."
        except ValueError:
            return "Task not found."
    
    def view_all_tasks(self):
        if len(self.lst) > 0:
            print("To-Do List:")
            for i, element in enumerate(self.lst, start=1):
                print(f"{i}. {element}")
            print("---------------------------------")
        else:
            print("Your to-do list is empty!")
    
    def update_task(self, old_task, new_task):
        if old_task in self.lst:
            index = self.lst.index(old_task)
            self.lst[index] = new_task
            return f"Task '{old_task}' updated to '{new_task}' successfully."
        else:
            return f"Task '{old_task}' not found."

my_list = to_do_list()

while True:
    print("1. Add task")
    print("2. Update task")
    print("3. Delete task")
    print("4. View To Do List")
    print("5. Exit list")
    user_input = int(input("Enter the number according to choice: "))
    
    if user_input == 1:
        add_task = input("Enter the task: ")
        print(my_list.add(add_task.title()))  
    
    elif user_input == 2:
        old_task = input("Enter the task you want to update: ")
        new_task = input("Enter the updated task: ")
        print(my_list.update_task(old_task.title(), new_task.title()))
       
    elif user_input == 3:
        remove_task = input("Enter the task: ")
        print(my_list.remove(remove_task.title()))

    elif user_input == 4:
        my_list.view_all_tasks()
    
    elif user_input == 5:
            print("Exiting Program")
            break

    else:
        print("Invalid input")
