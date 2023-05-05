try:

    x = int(input("Enter the first number: "))

    y = int(input("Enter the second number: "))

    if y == 0:

        raise ZeroDivisionError("Division by zero is not allowed")

    result = x / y
    print("Result: ", result)

except ValueError:

    print("Please enter valid integer numbers")

except ZeroDivisionError as e:

    print(e)
