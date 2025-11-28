# making a calculator!


def sub_add():

    a = float(input("enter first number!"))
    b = float(input("enter second number!"))

    print(a + b)

def mul():

    a = float(input("first number!"))
    b = float(input("second number"))

    print(a*b)

def div():

    a = float(input("enter dividend!"))
    b = float(input("enter divisor!"))

    print(a / b)

x = float(input("do you want to sub_add or mul or div ?!\n for sub_add press 1! \n for mul press 2! \n for div press 3!"))

if x == 1:
    sub_add()
elif x == 2:
    mul()
elif x == 3:
    div()
else:
    print("error, Try Again!")

print("thank you for using my calculator!")
print("last message just to prodce 3rd commit so i cna see on github")
