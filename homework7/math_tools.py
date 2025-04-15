def add(a, b):
    """
    Returns the sum of a and b
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference between a and b
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of a and b
    """
    return a * b

def divide(a, b):
    """
    Returns the quotient of a divided by b
    Raises error if b is 0
    """
    if b == 0:
        raise ZeroDivisionError("Can't divide by zero")
    return a / b