from project.song import Song
from typing import List


class Album:
    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.songs: List[Song] = list(songs)
        self.published: bool = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        song = next((s for s in self.songs if s.name == song_name), None)
        if song:
            self.songs.remove(song)
            return f"Removed song {song.name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]
        for song in self.songs:
            result.append(f"=={song.get_info()}")
        return '\n'.join(result)
