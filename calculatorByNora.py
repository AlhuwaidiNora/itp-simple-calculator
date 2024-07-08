

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Invalid value for denominator, can't divide by 0!"
    return a / b

def square(a):
    return a * a

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Invalid value, can't find the square root of a negative number!"
    return math.sqrt(a)
