print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")

