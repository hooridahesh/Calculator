
def add(numbers):
    ADD=0
    for x in numbers:
        x=int(x)
        ADD=x+ADD
    return (ADD)


print("Choose one of the options:")
print("0. Exit")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print()

while (1):
    choice=input("Enter choice:")
    if choice=="0":
        quit()
    if choice in ("1" or "2" or "3" or "4"):
        print("Enter your numbers:")
        numbers=input().split()
        if choice=="1":
            print(add(numbers))
    else:
        print("This option is invalid")
