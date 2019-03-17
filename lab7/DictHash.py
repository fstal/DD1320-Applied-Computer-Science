class Song:

    def __init__(self, trackid, song_length, artist, song_name):
        self.trackid = trackid
        self.song_length = song_length
        self.artist = artist
        self.song_name = song_name

    def __lt__(self, other):
        return self.song_name < other.song_name

class HashNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value

class DictHash:

    def __init__(self):
        self.dictionary = {}


    def store(self, key, data):
        if key in self.dictionary:
            self.dictionary[key].append(data)
        else:
            self.dictionary[key] = [data]


    def search(self, key):
        """
        Checks for key in dict, if found returns True
        :param song_dict:
        :return:
        """
        """

        if key in song_dict:
            # for obj in song_dict[dict_key]:
            #    print(obj.song_name)
            return True
        else:
            # print("No such key exists in dictionary")
            return False
        """
        #dict.get("Katt", None)
        return self.dictionary.get(key)
