class Node:

    def __init__(self, value, higher = None, lower = None, parent = None):
        self.value = value
        self.higher = higher
        self.lower = lower
        self.parent = parent #Kanske ej behövs

    def __str__(self):
        return str(self.lower)

    def has_been_printed(self):
        print('Kanske inte behövs')


class Bintree:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, newvalue):
        self.node = Node(newvalue)
        if self.root == None:
            self.root = self.node
            print('root')
        else:
            place(self.root, self.node)

        """
        if self.root == None:
            self.root = Node(newvalue)
            #self.root.place(newvalue)
        else:
            if self.root.value > newvalue:
                if self.root.lower == None:
                    self.root.lower = newvalue
                else:

            else:
                self.root.higher = newvalue

            # self.newNode = Node(newvalue)
            #self.newNode.place(newvalue)

        print(self.newNode.value)
        """

    def __contains__(self, value):
        """
        return finns(self.root, value)
        """
        return('katt')

    def write(self, node):
        in_order(node)
        """
        skriv(self.root)
        print("\n")
        """

        return('katt')

def place(root, newNode):
    """
    if root == None:
        root = Node(newNode)
        # self.root.place(newNode)
    else:
    """

    if root.value > newNode.value:
        if root.lower == None:
            root.lower = newNode
            print('lower')
        else:
            place(root.lower, newNode)

    elif root.value == newNode.value:
        print('Value already exists')

    else:
        if root.higher == None:
            root.hihger = newNode
            print('higher')
        else:
            place(root.higher, newNode)

            # self.newNode = Node(newNode)
            # self.newNode.place(newNode)

"""
Ej klar
def in_order(root, parent):

    if root.lower != None:
        root.
        in_order(root.lower)
    else:
        print(root.value)
"""

tree = Bintree()
tree.put(4)
tree.put(3)
tree.put(5)
tree.put(2)
tree.put(1)
