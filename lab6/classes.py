
class Song:

    def __init__(self, trackid, song_length, artist, song_name):
        self.trackid = trackid
        self.song_length = song_length
        self.artist = artist
        self.song_name = song_name

    def __lt__(self, other):
        return self.song_name < other.song_name

