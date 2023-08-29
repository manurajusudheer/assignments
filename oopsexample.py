class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
       return x * y
    def divide(self, x, y):
       if y == 0:
           return "Cannot divide by zero"
       else:
           return x / y


# Creating an instance of the Calculator class
calculator = Calculator()

# Taking user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing calculations
print("Sum:", calculator.add(num1, num2))
print("Difference:", calculator.subtract(num1, num2))
print("Product:", calculator.multiply(num1, num2))
print("Quotient:", calculator.divide(num1, num2))