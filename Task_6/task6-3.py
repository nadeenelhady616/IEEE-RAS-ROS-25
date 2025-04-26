from calculator import Calculator
calc = Calculator()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"add: {calc.add(a, b)}")
print(f"subtract: {calc.subtract(a, b)}")
print(f"multiply: {calc.multiply(a, b)}")
print(f"divide: {calc.divide(a, b)}")
