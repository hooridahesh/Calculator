def add1(numbers):
    ADD=0
    for x in numbers:
        x=int(x)
        ADD=x+ADD
    return (ADD)
"""
def subtract1(numbers):
    sub=0
    for x in numbers:
        x=int(x)
        sub=sub-x
    return (sub)
"""
def multiplication1(numbers):
    mul=1
    for x in numbers:
        x=int(x)
        mul=x*mul
    return (mul)

#def divide1(numbers):


print("Choose one of the options:")
print("0. Exit")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Divide")
print()

while (1):
    choice=input("Enter choice:")
    if choice=="0":
        quit()
    if choice in ("1" , "2" , "3" , "4"):
        print("Enter your numbers:")
        numbers=input().split()
        if choice=="1":
            print("The sum of the numbers is equal to {}".format(add1(numbers)))
        #elif choice=="2":
         #   print("The subtract of the numbers is equal to {}".format(subtract1(numbers)))
        elif choice == "3":
            print("The multiply of the numbers is equal to {}".format(multiplication1(numbers)))
        #elif choice=="4":
         #   print("The subtract of the numbers is equal to {}".format(divide1(numbers)))

    else:
        print("This option is invalid")
