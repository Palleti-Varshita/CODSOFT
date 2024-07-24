while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Choose the operation of your choice: (+, -, *, /, %, //, **): ")
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Division by zero is not allowed")
    elif operation == '%':
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    elif operation == '//':
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")
    elif operation == '**':
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result}")
    else:
        print("Invalid operation.")
    again = input("Do you want to perform another calculation? (Yes/No): ")
    if again.lower() != 'yes':
        break
