"""
plan -
    input for user to choose what calc method
    check if calc method is in class: if not ask to re-input
    ask for nums seperately and assign them variables
    return calc

todo -
    how to take different number of args (dynamic)
    how to implement order of operations
"""

class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            "You can't divide by zero"
        else:
            return self.a / self.b


calc_1 = Calculator(2, 6)
print(Calculator.divide(calc_1))