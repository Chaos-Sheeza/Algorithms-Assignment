# Class for nodes. Contains the value, and the right and left variables will store other nodes.
class Node:
    def __init__(self, x=None):
        self.value = x
        self.left = None
        self.right = None


# Class that builds a binary search tree.
class BST:
    def __init__(self):
        self.root = None

    # Insert method uses a private insert method so that the root node is set, and the private method adds the rest of
    # the nodes to it. If the root is set then it will call the private function, and if the value is smaller then it
    # will create a new node on the left and if larger on the right. If the node to be created is already occupied, then
    #  it recursively calls the method using the occupied node as the root.
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

    # The display method should also be recursive, using the next node to print, as the root each time (First all the
    # left then all the right nodes).
    # If conditions used to display empty nodes as well.
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


arr = [5, 4, 6, 3, 9, 1, 2, 8, 7, 10, 11, -1]
test = BST()
for i in arr:
    Node(i)
    test.insert(i)

test.display()
