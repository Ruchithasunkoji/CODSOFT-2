def calculator():
    # Prompt the user for input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric 5values.")
        return

    # Prompt the user for an operation
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the number corresponding to the operation: ")

    # Perform the calculation
    if operation == '1':
        result = num1 + num2
        operator = '+'
    elif operation == '2':
        result = num1 - num2
        operator = '-'
    elif operation == '3':
        result = num1 * num2
        operator = '*'
    elif operation == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operator = '/'
    else:
        print("Invalid operation. Please select a valid option.")
        return

    # Display the result
    print(f"The result of {num1} {operator} {num2} is: {result}")

# Run the calculator function
calculator()
