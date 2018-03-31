class Node:
    def __init__(self, x=None):
        self.value = x
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self.pInsert(x, self.root)

    def pInsert(self, x, node):
        if x < node.value:
            if node.left is None:
                node.left = Node(x)
            else:
                self.pInsert(x,node.left)
        elif x > node.value:
            if node.right is None:
                node.right = Node(x)
            else:
                self.pInsert(x,node.right)

    def display(self):
        if self.root is not None:
            self.pDisplay(self.root)

    def pDisplay(self, node):
        if node is not None:
            if node.left is None and node.right is not None:
                print("Value = %s \t\t" % node.value + "Left = %s \t" % node.left + "Right = %s \t" % node.right.value)
            elif node.left is not None and node.right is None:
                print("Value = %s \t\t" % node.value + "Left = %s \t\t" % node.left.value + "Right = %s \t" % node.right)
            elif node.left is not None and node.right is not None:
                print("Value = %s \t\t" % node.value + "Left = %s \t\t" % node.left.value + "Right = %s \t" % node.right.value)
            else:
                print("Value = %s \t\t" % node.value + "Left = %s \t" % node.left + "Right = %s \t" % node.right)
            self.pDisplay(node.left)
            self.pDisplay(node.right)



arr = [5,4,6,3,9,1,2,8,7,10,11,-1]
test = BST()
for i in arr:
    Node(i)
    test.insert(i)

test.display()