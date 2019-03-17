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
        newNode.next = None                 # The last node in a queue doesn't have any "next"
        if self.__firstnode == None:        # If there is no __firstnode our newNode becomes __firstnode
            self.__firstnode = newNode
            self.__activenode = self.__firstnode
            self.__lastnode = newNode

        else:                               # If there already is a __firstnode our newNode is the last node in the queue
            self.__lastnode.next = newNode  # Gives the previous __lastnode a __lastnode.next
            self.__lastnode = newNode       # Sets the new __lastnode to newNode

    def getValuePair(self):
        value_pair = [self.__activenode.value, self.peek()]
        self.__activenode = self.__activenode.next
        return value_pair

    def peek(self):
        if self.__activenode.next is None:
            return None
        else:
            return self.__activenode.next.value

    def dequeue(self):
        """
        Removes the first node in the queue
        Returns the value of the first node
        """
        temp = self.__firstnode                     # Saves the value of the __firstnode before we change the first node
        self.__firstnode = self.__firstnode.next    # sets the first node equal to the second node
        return temp

    def isEmpty(self):
        """
        Cecks if the queue is empty by checking if there is a __firstnode
        Returns True if empty and False otherwise
        """
        return self.__firstnode == None

class Syntaxfel(Exception):
    pass

    """
    Generar en print när något strider mot syntaxen som beskriver vad som var fel
    Ex. "Saknad stor bokstav", "För litet tal vid radslutet"

    """
    pass