list1=[]

def vieww():
    if not list1 :
        print("Your to-do list is empty")
    else:
        print("\nYour to-do list:")
        for i in range (0,len(list1)):
            print(i+1,list1[i])
            i+=1

def add():
    a=input("Enter your task: ")
    list1.append(a)
    print("Your task is added successfully")

def update():
    vieww()
    a=int(input("Enter the task to be updated: "))
        
    while(1>a>len(list1)):
        print("not a valid index")
        a=int(input("Enter the task to be updated: "))

    b=input("Write the updated task: ")
    list1[a-1]=b
    print("Your task is updated successfully.")

def remove():
    vieww()
    a=int(input("Enter the task you wanna remove: "))

    while(1>a>len(list1)):
        print("not a valid index")
        a=int(input("Enter the task you wanna remove: "))

    list1.remove(list1[a-1])
    print("Your task is removed successfully.")

while True:
    
    print("\n1. View my list\n2. Add a task\n3. Update a task\n4. Remove the task\n5. Exit the to-do list\n")

    choice=int(input("Choose your option: "))

    if choice==1 :
        vieww()
    elif choice==2:
        add()
    elif choice==3:
        update()
    elif choice==4:
        remove()
    elif choice==5:
        print("Exiting the list")
        break
    else:
        print("Invalid input")
    

