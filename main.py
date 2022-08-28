class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)

    def style_text(code):
        return "\33[{code}m".format(code=code)

    def color_text(code):
        return "\33[{code}m".format(code=code)

def add1(numbers):
    ADD=0
    for x in numbers:
        x=int(x)
        ADD=x+ADD
    return (ADD)

def subtract1(numbers):
    sub=int(numbers[0])
    subb=[]
    for y in range(1,len(numbers)):
        subb.append(numbers[y])
    for x in subb:
        x=int(x)
        sub=sub-x
    return (sub)

def multiplication1(numbers):
    mul=1
    for x in numbers:
        x=int(x)
        mul=x*mul
    return (mul)

def division1(numbers):
    div=int(numbers[0])
    ddiv=[]
    for y in range(1,len(numbers)):
        ddiv.append(numbers[y])
    for x in ddiv:
        x=int(x)
        div=div/x
    return (div)


print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(36) + "Choose one of the options:")
print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(33) + "0. Exit")
print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(33) + "1. Add")
print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(33) + "2. Subtract")
print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(33) + "3. Multiplication")
print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(33) + "4. Division")
print()

while (1):
    choice=input(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(35) + "Enter choice:")
    if choice=="0":
        quit()
    if choice in ("1" , "2" , "3" , "4"):
        print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(34) + "Enter your numbers:")
        numbers=input().split()
        if choice=="1":
            print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(0) + "The sum of the numbers is equal to {}".format(add1(numbers)))
        elif choice=="2":
            print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(0) + "The subtract of the numbers is equal to {}".format(subtract1(numbers)))
        elif choice == "3":
            print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(0) + "The multiply of the numbers is equal to {}".format(multiplication1(numbers)))
        elif choice=="4":
            print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(0) + "The division of the numbers is equal to {}".format(division1(numbers)))

    else:
        print(ANSI.background(97) + ANSI.color_text(0) + ANSI.style_text(31) + "This option is invalid")

