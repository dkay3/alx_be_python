# match_case_calculator.py

def calculate(num1, num2, operator):
    result = None
    operation = None

    match operator:
        case '+':
            result = num1 + num2
            operation = 'addition'
        case '-':
            result = num1 - num2
            operation = 'subtraction'
        case '*':
            result = num1 * num2
            operation = 'multiplication'
        case '/':
            if num2 == 0:
                return None, 'Cannot divide by zero.'
            result = num1 / num2
            operation = 'division'
        case _:
            return None, f'Invalid operator: {operator}'

    return result, f'{num1} {operator} {num2} = {result} (Operation: {operation})'

def main():
    print("Welcome to the Match Case Calculator!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Choose the operation (+, -, *, /): ")

            result, message = calculate(num1, num2, operator)

            if result is None:
                print(f'Error: {message}')
            else:
                print(f'The result is {result}.')
            break

        except ValueError:
            print("Error: Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main()
