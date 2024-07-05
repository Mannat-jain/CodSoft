#Random password generator
import random
import string

def password(a):
    n=string.ascii_letters+string.digits+string.punctuation

    password=[random.choice(string.ascii_lowercase),random.choice(string.ascii_uppercase),random.choice(string.digits),random.choice(string.punctuation)]
    password+=random.choices(n,k=a-4)

    random.shuffle(password)

    return "".join(password)


print("Generating a random password\n")
a=int(input("Length of password: "))
if(a<4):
    print("Password should be at least 4 characters long.")
else:
    p=password(a)
    print("Generated password =",p)
