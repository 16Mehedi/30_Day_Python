while True:
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter 2nd number: "))

    print("Choose operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice(1/2/3/4): ")

    if choice == "1":
        result = num1 + num2
        print("Result =", result)
    elif choice == "2":
        result = num1 - num2
        print("Result =", result)
    elif choice == "3":
        result = num1 * num2
        print("Result =", result)
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print("Result =", result)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid input")

    # Ask if user wants to continue
    again = input("Do you want to calculate again? answer Yes or No: ").lower()
    if again != "yes":
        print("Goodbye")
        break
