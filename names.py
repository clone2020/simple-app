#!/use/bin/python

def checkName(name):
    checkName = input("Is your name, " + name + " ? ")

    if checkName.lower() == "yes":
        print("hello ,", name)
    else:
        print("we are sorry! ,", name)
        name = input("What is your name again ? ")
        print("Welcome, ", name)

checkName("rudra")