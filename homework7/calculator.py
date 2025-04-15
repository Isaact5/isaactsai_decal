import math_tools

def main():
    # Ask for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Ask for operation
        print("\nOperations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        operation = input("\nType the number corresponding to the operation you want to perform: ")
        
        # Perform calculation based on chosen operation
        if operation == "1":
            result = math_tools.add(num1, num2)
            print(f"\n{num1} + {num2} = {result}")
        elif operation == "2":
            result = math_tools.subtract(num1, num2)
            print(f"\n{num1} - {num2} = {result}")
        elif operation == "3":
            result = math_tools.multiply(num1, num2)
            print(f"\n{num1} * {num2} = {result}")
        elif operation == "4":
            try:
                result = math_tools.divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")
            except ZeroDivisionError as e:
                print(f"\nError: {e}")
        else:
            print("\nInvalid input, try again!")
            
    except ValueError:
        print("\nError: Please enter valid numbers")

if __name__ == "__main__":
    main()