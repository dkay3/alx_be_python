# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations: addition, subtraction, multiplication, division.
    
    Parameters:
    - operand1 (float): The first operand
    - operand2 (float): The second operand
    - operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
    - float: The result of the arithmetic operation
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'")
