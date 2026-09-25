print("Python Calculator")

while True:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = num1 / num2
        else:
            print("Invalid operator.")
            continue

        print("Result:", result)

        again = input("Do you want to calculate again? (y/n): ")
        if again.lower() != "y":
            print("Goodbye!")
            break

    except ValueError:
        print("Invalid input. Please enter numbers.")
