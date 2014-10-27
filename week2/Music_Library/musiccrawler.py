from os import listdir
from os.path import isfile, join
from mutagen.mp3 import MP3
from playlist import Playlist
from song import Song


class MusicCrawler:

    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        playlist = Playlist(self.path)
        for music_file in files:
            directory = self.path + music_file
            audio = MP3(directory)
            title = music_file.split(".")[0]
            artist = str(audio.tags["TALB"])
            album = str(audio.tags["TIT2"])
            length = int(audio.info.length)
            bitrate = int(audio.info.bitrate)
            song = Song(
                title,
                artist,
                album,
                Song.MAX_RATING,
                length,
                bitrate
            )
            playlist.add_song(song)

        return playlist
