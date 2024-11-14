Options = ["List the Constituency" , "List the region", "List the Constuency type", "List the valid votes","Vote"]

print("Welcome to the Election, it's great to have you here")
print("Choose your option(please intput a number)")
print("Option Number\tOption")
optionNumber = 0
for option in Options:
    print(optionNumber,"\t\t",option)
    optionNumber += 1
int(input("What is your option?"))
