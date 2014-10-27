from playlist import Playlist
from song import Song


class MusicPlayer:

    def __init__(self):
        self.playlist = Playlist("Playlist")


def main():
    player = MusicPlayer()
    command = input("Enter command> ")
    command = command.split(" ")
    if command[0] == "add":
        self.playlist.add_song(command[1])

if __name__ == "__main__":
    main()
