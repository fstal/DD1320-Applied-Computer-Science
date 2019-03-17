import array

class ArrayQ:
    """
    A class for our array
    """
    def __init__(self):
        """
        Creates a new array
        """
        self.__myArray = array.array('i')

    def enqueue(self, num):
        """
        Adds an element to the end of our array with the value num
        """
        self.__myArray.append(num)

    def dequeue(self):
        """
        Removes the first element in our array and returns it
        """
        return self.__myArray.pop(0)

    def isEmpty(self):
        """
        Checks if the array is empty
        """
        return not self.__myArray
