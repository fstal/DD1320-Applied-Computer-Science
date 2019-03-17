class LinkedQ:
    """
    Class for our queue of nodes. Contains two private attributes which refrences to the first and last node in the queue
    """

    def __init__(self):
        self.__firstnode = None
        self.__lastnode = None
        self.__activenode = self.__firstnode

    def enqueue(self, x):
        """
        Creates a new node and places it last in the queue.
        If it's the only node in the queue it is also saved to __firstnode
        x = the value of the node
        """
        newNode = Node(x)
        newNode.next = None  # The last node in a queue doesn't have any "next"
        if self.__firstnode is None:  # If there is no __firstnode our newNode becomes __firstnode
            self.__firstnode = newNode
            self.__activenode = self.__firstnode
            self.__lastnode = newNode

        else:  # If there already is a __firstnode our newNode is the last node in the queue
            self.__lastnode.next = newNode  # Gives the previous __lastnode a __lastnode.next
            self.__lastnode = newNode  # Sets the new __lastnode to newNode

    def getValuePair(self):
        """
        Metod used for Lab8, returns a list with two elements
        The first being our current_value and the second
        being the next - or the the so called peek_value
        :return:
        """
        value_pair = [self.__activenode.value, self.peek()]
        self.__activenode = self.__activenode.next
        return value_pair

    def peek(self):
        """
        peek() the way we figured it should be used in Lab9. Returns None
        if self activenode is actually None (circumventing the NoneType error thingie)
        :return:
        """
        if self.__activenode is not None:
            return self.__activenode.value
        else:
            return None


    def dequeue(self):
        """
        Removes the first node in the queue
        Returns the value of the first node
        """
        temp = self.__firstnode  # Saves the value of the __firstnode before we change the first node
        self.__firstnode = self.__firstnode.next  # sets the first node equal to the next node
        self.__activenode = self.__firstnode
        return str(temp)

    def isEmpty(self):
        """
        Checks if the queue is empty by checking if there is a __firstnode
        Returns True if empty and False otherwise
        """
        return self.__firstnode is None

    def __str__(self):
        """
        Borrowed with modifications from lesson 10, TILDA.
        :return:
        """
        if self.isEmpty():
            return ''
        else:
            self.__activenode = self.__firstnode
            remaining_q = str(self.__activenode.value)
            while self.__activenode is not self.__lastnode:
                remaining_q += str(self.__activenode.next.value)
                self.__activenode = self.__activenode.next
            self.__activenode = self.__firstnode
        return remaining_q


class Node:
    """
    Class for each Node which contains the nodes value and a reference to the node next to it

    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        """
        Returns the value of the node
        """
        return str(self.value)


class Syntaxfel(Exception):
    """
    Inherits from Exception. We raise this when something isnt correct according to syntax
    raised with a print describing the error
    Eg. 'Saknad stor bokstav', 'För litet tal vid radslutet'
    """
    pass


class Ruta:
    def __init__(self, atom="()", num=1):
        self.first_ruta = None
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

    #def __str__(self):
    #    return str(self.atom) + str(self.num)