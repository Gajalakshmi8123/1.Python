def add_task(task):
    tasks=input("add a task")
    task.append(tasks)
    print("The added task",task)

def view_task(tasks):
        if tasks:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            else:
                print("No tasks added yet.")


def main():
    task=[]
    while True:
        
        choice=int(input("Enter the number: "))
       
        if choice==1:
            print("result",add_task(task))

        elif choice==2:
            print("view",view_task(task))
        
        elif choice==3:
            print("sucessfully completed")
            break

        else:
            print("Invalid condition")

main()
