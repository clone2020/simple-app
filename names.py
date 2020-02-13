#!/use/bin/python

def checkName(name):
    checkName = input("Is your name, " + name + " ? ")

    if checkName.lower() == "yes":
        print("hello ,", name)
    else:
        print("we are sorry! ,", name)

checkName("rudra")
