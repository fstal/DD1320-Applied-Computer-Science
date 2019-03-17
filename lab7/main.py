from classes import HashTable, Song, HashNode
from DictHash import DictHash
from LinkedQ import LinkedNode, LinkedQ
import timeit


def song_reader():
    """
    Reads file, splits rows by the separator to a list and sends row
    by row to object_creator()
    :return:
    """
    with open('unique_tracks.txt', 'r') as read:
        for row in read:
            row_list = row.strip().split('<SEP>')
            object_creator(row_list)


def object_creator(row_list):
    """
    Takes row_lists and creates a Song-object.
    Adds these to a separate dictionary and a list
    :param row_list:
    :return:
    """
    object = Song(row_list[0], row_list[1], row_list[2], row_list[3])
    object_list.append(object)
    node = HashNode(row_list[2], object)
    table.put(node)


def dict_search(search_key):
    """
    Checks for key in dict, if found returns the values for that key
    :param song_dict:
    :return:
    """
    my_dict.search(search_key)


def timer_all():
    """
    Measures time for all dem functions
    :return:
    """
    #dict_fill = timeit.timeit(stmt=lambda: song_reader(), number=5)
    #print("Dict_fill took ", round(dict_fill, 4), "seconds")
    #search = timeit.timeit(stmt=lambda: dict_search('ashdhusagd'), number=50000)
    #print("Dict_fill took ", round(search, 4), "seconds")
    search = timeit.timeit(stmt=lambda: table.find('Faster Pussy cat'), number=50000)
    print("Searching the dict took ", round(search, 4), "seconds")


object_list = []
my_dict = DictHash()
table = HashTable()
song_reader()

#timer_all()
print(table.find('Aerosmith'))
#print(table.find('Faster Pussy cat', 'Silent Night'))
print(table.collisioncount())
"""
For testing all the artists in the file
for spot in object_list:
    table.find(spot.artist)
"""


"""
Analysis

Filling the dictionary:
Filling the dictionary with the songs in the file took about 0.5 seconds longer than in the other version.

Searching in the dictionary:
Searching 50000 times took about 0.04 sec compared to the 0.01 sec it took in the other version.

Collisions:
We get 13094 collisions in our table. This means that less than 10% of the total artists are colliding.
This can be made even better with a better hash-function.


145349

"""
