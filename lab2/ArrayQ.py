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
        print(self.__myArray)

    def dequeue(self):
        """
        Removes the first element in our array and returns it
        """
        x = self.__myArray.pop(0)
        return x

    def isEmpty(self):
        """
        Checks if the array is empty
        """
        return not self.__myArray







a.enqueue(1)
a.enqueue(2)
x = a.dequeue()
y = a.dequeue()
print(a.isEmpty())
print(x, y)   # 1 2 ska komma ut