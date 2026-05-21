# My first calculator again
print("===== Simple Calculator =====")

while True:

    # First Number
    while True:
        try:
            a = float(input("Enter first number:- "))
            break
        except ValueError:
            print("Please enter numbers only")

    # Second Number
    while True:
        try:
            b = float(input("Enter second number:- "))
            break
        except ValueError:
            print("Please enter numbers only")

    # Menu
    print("\n1 = Addition (+)")
    print("2 = Subtraction (-)")
    print("3 = Multiplication (*)")
    print("4 = Division (/)")
    print("5 = Exit")

    c = input("Enter your choice:- ")

    if c == "5":
        print("Calculator closed")
        print("Thanks for using our calculator")
        break

    elif c == "1":
        print("Your answer is =", a + b)

    elif c == "2":
        print("Your answer is =", a - b)

    elif c == "3":
        print("Your answer is =", a * b)

    elif c == "4":

        if b == 0:
            print("Cannot divide by zero")

        else:
            print("Your answer is =", a / b)

    else:
        print("Please choose between 1 to 5")
