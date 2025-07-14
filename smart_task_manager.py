print("🧠 Welcome to Smart Task Manager")
name = input("Enter your name: ")
print(f"Hi {name.capitalize()}, let's manage your tasks!")
task_list = []
task_count=int(input("Enter the number of tasks to be added: "))
for i in range(task_count):
    task_name= input (f"Enter the task name {i+1}: ").lower()
    task_list.append(task_name)
add_task=input(("Do you want to add more tasks?  y / n\n" ))
if add_task== 'y':
    updatedtask_count=int(input("Enter the number of tasks to be added more: "))
    for i in range(updatedtask_count):
        pos=int(input("Which position: "))
        if pos <= 0 or pos > len(task_list) + 1:
            print("❌ Invalid position! Task will be added to the end.")
            task_name= input("Enter the task name: ").lower()
            task_list.append(task_name)
        else:
            task_name= input("Enter the task name: ").lower()
            task_list.insert((pos-1),task_name)
else:
   print ()
print("Your tasks are: ")
for i in range(len(task_list)):
    print(f"{i+1} : {task_list[i].capitalize()}")    

print("Do you want to: \n 1. Remove the task by name \n 2. Remove the task by position")
remove_input=int(input("Enter 1 or 2: "))
if remove_input==1:
    task_to_remove = input("Enter the task name to remove: ")
    if task_to_remove.lower() in task_list:
        task_list.remove(task_to_remove.lower())
        print(f"'{task_to_remove.lower()}' removed from the list.")
    else:
        print(f"'{task_to_remove}' was not found in the task list.")
else:
    
    pos_task_to_remove = int(input("Enter the position of task to remove: "))
    if 1 <= pos_task_to_remove <= len(task_list):
        TaskRemoved=task_list.pop(pos_task_to_remove-1)
        print(f"'{TaskRemoved.capitalize()}' removed from the list.")
    else: 
        print("❌ Invalid position. No task removed.")    
print("Your tasks are: ")
for i in range(len(task_list)):
    print(f"{i+1} : {task_list[i].capitalize()} ") 
