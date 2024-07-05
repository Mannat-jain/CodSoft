#Contact Book
contact =[]
phone=[]
mail=[]
address=[]

def vieww():
    if not contact:
        print("There's no contact in contact book.")
    else:
        for i in range(0,len(contact)):
            print(i+1,contact[i],phone[i],mail[i],address[i])

def add():
    a=input("Add the name: ")
    b=int(input("Add the phone: "))
    c=input("Add the mail: ")
    d=input("Add the address: ")
    contact.append(a)
    phone.append(b)
    mail.append(c)
    address.append(d)
    print("\nYour contact is added successfully.")

def update():
    vieww()
    n=int(input("Mention the contact index you wanna update: "))
    o=input("What do you wanna update from the following list: name,number,mail,address? ").lower()
    if(o=="name"):
        a=input("Name: ")
        contact[n-1]=a
    elif(o=="number"):
        a=input("Number: ")
        phone[n-1]=a
    elif(o=="mail"):
        a=input("Mail: ")
        mail[n-1]=a
    elif(o=="address"):
        a=input("Address: ")
        address[n-1]=a
    else:
        print("Invalid choice")

    print("\nYour contact is updated successfully.")

def remove():
    vieww()
    n=int(input("Mention the contact index you wanna remove: "))
    contact.remove(contact[n-1])
    phone.remove(phone[n-1])
    mail.remove(mail[n-1])
    address.remove(address[n-1])

    print("\nYour contact is removed successfully. ")

print("Welcome to your conatct book!!!")
while True:
    
    print("\n1. View my contact book\n2. Add a contact\n3. Update a contact\n4. Remove the contcat\n5. Exit the contact book\n")

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
        print("Exiting the contact book")
        break
    else:
        print("Invalid input")
