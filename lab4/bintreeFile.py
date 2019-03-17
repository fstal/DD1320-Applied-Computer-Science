
class Node:
    """
    Class for each Node, containing attributes for a value, a right-reference and a left reference
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def search(self, x):
        """
        Traverses our tree starting from the root checking if x ever is equal to the value of the node
        :param x:
        :return:
        """
        if self.value == x:
            #print("You looked for " + str(x) + ", that element does exist in our search tree")
            return True
        elif self.value > x:
            if self.left:
                return self.left.search(x)
            else:
                #print("You looked for " + str(x) + ", no such element exists")
                return False
        else:
            if self.right:
                return self.right.search(x)
            else:
                #print("You looked for " + str(x) + ", no such element exists")
                return False

    def putta(self, newvalue):
        """
        Recursive method that will work its way down the tree until it finds the correct spot to insert a new node
        with newvalue as its value. Return True only once it succeeds in adding a new node, returns False only if
        a node with that value already exists.
        :param newvalue:
        :return:
        """
        if self.value == newvalue:
            #print("A node with the value " + str(newvalue) + " already exists")   #for test
            return False
        elif self.value > newvalue:
            if self.left:                               #checks if left chld exists
                return self.left.putta(newvalue)        #if left child exists, calls insert on that child
            else:
                self.left = Node(newvalue)
                return True
        else:
            if self.value < newvalue:
                if self.right:                          #checks if left chld exists
                    return self.right.putta(newvalue)  #--=--
                else:
                    self.right = Node(newvalue)
                    return True

    def inorder(self):
        """
        Basically moves down the tree recursively to the furthest left,
        if no more self.left exists it prints the value of that node,
        it then tries to move right. Rinse, repeat.
        :return:
        """
        if self.left:
            self.left.inorder()
        print(str(self.value))
        if self.right:
            self.right.inorder()


class Bintree:
    """
    A class for our binary search tree
    """

    def __init__(self):
        """
        Initiates our binary tree
        """
        self.root = None

    def put(self, newvalue):
        """
        Checks if there's a root, if True calls our putta() method with newvalue as input
        If no root, creates a new node with newvalue and makes it our root
        :param newvalue:
        :return:
        """
        if self.root:
            return self.root.putta(newvalue)
        else:
            self.root = Node(newvalue)
            return True

    def __contains__(self, x):
        """
        Checks if root exists, calls search() method if that is the case
        :param x:
        :return:
        """
        if self.root:
            return self.root.search(x)
        else:
            #print("You looked for " + str(x) + ", no such element exist... actually there are no elements dumbass")
            return False

    def write_inorder(self):
        """
        Checks if root exists, calls inorder() if that is the case
        :return:
        """

        if self.root:
            self.root.inorder()
        else:
            print("Nope, gtfo, tengo no roots")
            return False


tree = Bintree()
#tree.write_inorder()           #test
"""
tree.put(5)
tree.put(3)
tree.put(1)
tree.put(4)
tree.put(1)
tree.put(7)
tree.put(6)
tree.put(9)
tree.write_inorder()
"""

"""
Vaaarför försöker ni tvinga oss att använda en mix av engelska och svenska metod- och funktionsnamn??
It's so darn ugly!
"""