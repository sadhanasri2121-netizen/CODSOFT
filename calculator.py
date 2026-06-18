print("=================================")
print("     CODSOFT CALCULATOR")
print("=================================")

while True:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    print("\nChoose Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

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
            print("Error! Division by zero is not allowed.")

    else:
        print("Invalid Choice!")

    again = input("\nDo you want to calculate again? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using CodSoft Calculator!")
        break
