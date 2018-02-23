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


def rpn(calc):
    calculation = 0
    operator = calc.pop()
    num = int(calc.pop())
    if len(calc.items) > 1:
        num2 = rpn(calc)
    else:
        num2 = int(calc.pop())

    if operator == "+":
        calculation = num2+num
    elif operator == "-":
        calculation = num2-num
    elif operator == "*":
        calculation = num2*num
    elif operator == "/":
        calculation = num2/num
    return calculation


user = Stack()
userInput = raw_input("Enter a calculation in RPN\n").split(" ")
for i in userInput:
    user.push(i)
print(" = %d" % (rpn(user)))
