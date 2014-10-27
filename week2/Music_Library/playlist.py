import json
from song import Song


class Playlist:

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        objects_to_remove = []
        for index, song in enumerate(self.songs):
            if song.title == song_name:
                objects_to_remove.append(song)

        for obj in objects_to_remove:
            self.songs.remove(obj)

    def total_length(self):
        in_seconds = 0
        for song in self.songs:
            in_seconds += song.length

        minutes = in_seconds // 60
        seconds = in_seconds % 60
        return("{}:{}".format(minutes, seconds))

    def remove_disrated(self, rating):
        objects_to_remove = []
        for index, song in enumerate(self.songs):
            if song.rating < rating:
                objects_to_remove.append(song)

        for obj in objects_to_remove:
            self.songs.remove(obj)

    def remove_bad_quality(self):
        objects_to_remove = []
        for index, song in enumerate(self.songs):
            if song.bitrate < 320000:
                objects_to_remove.append(song)

        for obj in objects_to_remove:
            self.songs.remove(obj)

    def show_artists(self):
        artists = set()
        for song in self.songs:
            artists.add(song.artist)

        return artists

    def save(self, filename):
        json_dict = {"name": self.name, "songs": []}
        for song in self.songs:
            song_dict = {}
            song_dict = song.__dict__
            json_dict["songs"].append(song_dict)

        json_dict = json.dumps(json_dict, indent=4)
        file = open(filename, "w")
        file.write(json_dict)
        file.close()

    @staticmethod
    def load(filename):
        file = open(filename, "r")
        playlist_dict = json.loads(file.read())
        file.close()
        playlist = Playlist(playlist_dict["name"])
        for song in playlist_dict["songs"]:
            new_song = Song(
                song["title"],
                song["artist"],
                song["album"],
                song["rating"],
                song["length"],
                song["bitrate"]
            )
            playlist.add_song(new_song)

        return playlist

    def __str__(self):
        song_info = []
        for song in self.songs:
            minutes = song.length // 60
            seconds = song.length % 60
            duration = "{}:{}".format(minutes, seconds)
            song_repr = "{} {} - {}".format(song.artist, song.title, duration)
            song_info.append(song_repr)

        return "\n".join(song_info)
