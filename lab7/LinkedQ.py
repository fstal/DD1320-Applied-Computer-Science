class LinkedNode:
    """
    Class for each Node which contains the nodes value and a reference to the next node

    """
    def __init__(self, artist=None, next=None):
        self.artist = artist
        self.song_objects = []
        self.next = next



class LinkedQ:
    """
    Class for our queue of nodes. Contains two private attributes which refrences to the first and last node in the queue
    """
    def __init__(self):
        self.__firstnode = None
        self.__lastnode = None
        self.__activenode = self.__firstnode
        self.num = 0


    def enqueue(self, artist, node):
        """
        Creates a new node and places it last in the queue.
        If it's the only node in the queue it is also saved to __firstnode
        x = the value of the node
        """
        newNode = LinkedNode(artist)
        newNode.song_objects.append(node.value)
        newNode.next = None                 # The last node in a queue doesn't have any "next"
        if self.__firstnode == None:        # If there is no __firstnode our newNode becomes __firstnode
            self.__firstnode = newNode
            self.__activenode = self.__firstnode
            self.__lastnode = newNode
        else:                               # If there already is a __firstnode our newNode is the last node in the queue
            self.__lastnode.next = newNode  # Gives the previous __lastnode a __lastnode.next
            self.__lastnode = newNode       # Sets the new __lastnode to newNode


    def linkedTraverse(self, node):
        if node.key == self.__activenode.artist:
            self.__firstnode.song_objects.append(node.value)
            self.__activenode = self.__firstnode
            return False
        elif self.__activenode.next is None:
            self.enqueue(node.key, node)
            self.__activenode = self.__firstnode
            return True
        else:
            self.__activenode = self.__activenode.next
            #print('kaka')
            self.linkedTraverse(node)

    def linkedFind(self, search_key):
        if self.__activenode.artist == search_key:
            self.__activenode = self.__firstnode
            #print(self.num)
            return 'Found you'
        elif self.__activenode.next is None:
            self.__activenode = self.__firstnode
            raise KeyError
        else:
            self.num += 1
            self.__activenode = self.__activenode.next
            self.linkedFind(search_key)
            #return 'Artist not in list'
