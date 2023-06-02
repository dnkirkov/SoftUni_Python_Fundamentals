# Create a function that receives three parameters, calculates a result depending on the given operator, and returns
# it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers. The operator can be one
# of the following: "multiply", "divide", "add", "subtract"

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return int(a / b)


def calculator():
    operations = ["add", "subtract", "multiply", "divide"]
    command = input()
    num1 = int(input())
    num2 = int(input())
    if command == operations[0]:
        print(add(num1, num2))
    elif command == operations[1]:
        print(subtract(num1, num2))
    elif command == operations[2]:
        print(multiply(num1, num2))
    elif command == operations[3]:
        print(divide(num1, num2))


calculator()