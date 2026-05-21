# My first calculator again

print("For starting calculator press any alphabet or number")
e = input("press number/alphabet to start:- ")
print("If you want to exit the calculator press 5")
while True:
    while True:
        try:
            a = float(input("Enter your first number:- "))
        except ValueError:
            print("Please choose only number not alphabets")
            continue
        break
    while True:
        try:  
            b = float(input("Enter your second number:- "))
        except ValueError:
            print("Please choose only number not alphabets")
            continue
        break

    print(("1 = plus'+', 2 = Minus'-', 3 = multiply'*', 4 = divide'/', 5 = Exit"))
    c = float(input("Enter you choice:- "))


    if c == 5:
        break
    elif c == 1:
        q = a + b
        print("Your answer is =", q)
    elif c == 2:
        q = a - b
        print("Your answer is =", q)
    elif c == 3:
        q = a * b
        print("Your answer is =", q)
    elif c == 4:
        if b != 0:
            q = a / b
            print("Your answer is =", q)
        else:
            print("Denominator cann't be zero'0'")
    else:
        print("Please choose a choice between 1 - 5")