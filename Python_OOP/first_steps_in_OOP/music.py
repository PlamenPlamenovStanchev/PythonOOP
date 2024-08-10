class Music:
    def __init__(self, tittle, artist, lyrics):
        self.tittle = tittle
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f"This is {self.tittle} from {self.artist}"

    def play(self):
        return self.lyrics


my_music = Music("Hit'em up", "Tupac Shakur", "...")
print(my_music.print_info())
print(my_music.play())