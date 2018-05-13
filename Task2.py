# Stack object, should be an array that functions as a stack. Only direct functionalities should be pop and push.
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# Method that takes 3 parameters, two ints and a string. Changes sting into an operator.
def operation(operator, num, num2):
    calculation = 0
    if operator == "+":
        calculation = num2+num
        print("Addition")
    elif operator == "-":
        calculation = num2-num
        print("Subtraction")
    elif operator == "*":
        calculation = num2*num
        print("Multiplication")
    elif operator == "/":
        calculation = num2/num
        print("Division")
    return calculation


'''
def RPNr(calc):
    operator = calc.pop()
    num = int(calc.pop())
    if len(calc.items) > 1:
        num2 = RPNr(calc)
    else:
        num2 = int(calc.pop())
    return operation(operator, num, num2)
'''


# RPN calculator function.
# Grabs the input stack and empties it in another stack in reverse. While the stack is not empty, the method checks if
# the first item is an operator, if not, then it stores the integers in the same input stack. If it find an operator, it
# pops two elements from the input stack, pops the operator from the other stack, calculates the operation, then pushes
# the result on that input stack.
def RPN(calc):
    store = Stack()
    for x in range(calc.size()):
        store.push(calc.pop())
    while not store.isEmpty():
        if store.peek() == '+' or store.peek() == '-' or store.peek() == '*' or store.peek() == '/':
            num = float(calc.pop())
            num2 = float(calc.pop())
            operator = store.pop()
            calc.push(operation(operator, num, num2))
            print(calc.items)
        else:
            calc.push(store.pop())
            print(calc.items)
    # If there is more than one element in the stack, then the user inputted an incorrect equation (missing operator).
    if calc.size() > 1:
        print("Syntax error")


user = Stack()
userInput = raw_input("Enter a calculation in RPN\n").split(" ")
for i in userInput:
    user.push(i)
try:
    RPN(user)
except:
    print("Syntax error")
