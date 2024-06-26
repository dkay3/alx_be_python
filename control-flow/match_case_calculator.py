# match_case_calculator.py

def calculate(num1, num2, operator):
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                return None, 'Cannot dvivide by zero.'
            result = num1 / num2
        case _:
            return None, f'Invalid operator: {operator}'

    return result, None

def main():
    print("Welcome to the Match Case Calculator!")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Choose the operation (+, -, *, /): ")

            result, error_message = calculate(num1, num2, operator)

            if error_message:
                print(f'Error: {error_message}')
            else:
                print(f'The result is {result}')

            break

        except ValueError:
            print("Error: Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    main()
