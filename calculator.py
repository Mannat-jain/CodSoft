print("Let's Calculate ")
a=int(input("Enter first number: "))
o=input("choose + , - , * , / , % , ** , // : ")
b=int(input("Enter second number: "))

if(o == "+"):
    print(a ,"+", b, "=", a+b)
elif(o == "-"):
    print(a ,"-", b, "=", a-b)
elif(o == "*"):
    print(a ,"*", b, "=", a*b)
elif(o == "/"):
    print(a ,"/", b, "=", a/b)
elif(o == "%"):
    print(a ,"%", b, "=", a%b)
elif(o == "**"):
    print(a ,"**", b, "=", a**b)
elif(o == "//"):
    print(a ,"//", b, "=", a//b)
else:
    print("Invalid Operator")
