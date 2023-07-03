def addition():
    try:
        num1 = float(input("Please enter the first number: \n"))
        num2 = float(input("Please enter the second number: \n"))
    except:
        print("Please enter valid numbers")
        addition()

    total = num1 + num2
    return total

