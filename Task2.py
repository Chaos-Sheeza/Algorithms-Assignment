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


def check(num):
    if num == "+" or num == "-" or num == "*" or num == "/":
        return False
    else:
        return True


def RPNr(calc):
    operator = calc.pop()
    num = int(calc.pop())
    if len(calc.items) > 1:
        num2 = RPNr(calc)
    else:
        num2 = int(calc.pop())
    return operation(operator, num, num2)


def RPNi(calc):
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
    if calc.size() > 1:
        print("Syntax error")


user = Stack()
userInput = raw_input("Enter a calculation in RPN\n").split(" ")
for i in userInput:
    user.push(i)
try:
    RPNi(user)
except:
    print("Syntax error")
