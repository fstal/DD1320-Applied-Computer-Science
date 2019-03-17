from LinkedQ import LinkedNode, LinkedQ

class Song:

    def __init__(self, trackid, song_length, artist, song_name):
        self.trackid = trackid
        self.song_length = song_length
        self.artist = artist
        self.song_name = song_name

    def __lt__(self, other):
        return self.song_name < other.song_name


class HashTable:

    def __init__(self):
        self.size = 145349
        self.slots = [None] * self.size
        self.collisions = 0

    def collisioncount(self):
        return self.collisions

    def create_hash(self, key):
        """
        Tagen ur föreläsning nr.. :
        :param key:
        :return:
        """
        result = 0
        for char in key:
            result = result * 32 + ord(char)
        return result

    def put(self, node):
        table_idx = self.create_hash(node.key) % self.size
        if self.slots[table_idx] is None:
            self.slots[table_idx] = LinkedQ()
            self.slots[table_idx].enqueue(node.key, node)
        else:
            num = self.slots[table_idx].linkedTraverse(node)
            if num:
                self.collisions += 1

    def find(self, search_key):
        table_idx = self.create_hash(search_key) % self.size
        if self.slots[table_idx] is None:
            raise KeyError
        else:
            return self.slots[table_idx].linkedFind(search_key)




class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value



"""
Du ska använda KeyError för att tala om att en nyckel inte finns
"""






"""
#temp = self.slots[table_idx]
#if len(temp) == 1:
#    return 'Found you without clashes'
else:
    for i in self.slots[table_idx]:
        if self.slots[table_idx][0] == key
            return 'Found you'
return "The artist and/or song doesn't excist"
"""