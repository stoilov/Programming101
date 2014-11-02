from playlist import Playlist
from song import Song
from musiccrawler import MusicCrawler


class MusicPlayer:

    def __init__(self):
        self.playlist = Playlist("Playlist")

    def print_messages(self):
        print("Hello, welcome to the music player interface!\n")
        print("Load your playlist!")

    def get_input(self):
        command = input("Enter command> ")
        command = command.split(" ")
        return command

    def interface(self):
        command = self.get_input()
        while command[0] != "exit":
            if command[0] == "load_dir":
                folder = MusicCrawler(command[1])
                self.playlist = folder.generate_playlist()
                command = self.get_input()
            elif command[0] == "remove_song":
                self.playlist.remove_song(command[1])
                print("Songs removed.")
                command = self.get_input()
            elif command[0] == "total_length":
                print(self.playlist.total_length())
                command = self.get_input()
            elif command[0] == "remove_disrated":
                self.playlist.remove_disrated(command[1])
                command = self.get_input()
            elif command[0] == "remove_song":
                self.playlist.remove_song(command[1])
                command = self.get_input()
            elif command[0] == "remove_bad_quality":
                self.playlist.remove_bad_quality()
                print("Songs removed.")
                command = self.get_input()
            elif command[0] == "show_artists":
                print(self.playlist.show_artists())
                command = self.get_input()
            elif command[0] == "remove_song":
                self.playlist.remove_song(command[1])
                command = self.get_input()
            elif command[0] == "save":
                self.playlist.save(command[1])
                command = self.get_input()
            elif command[0] == "load":
                self.playlist = self.playlist.load(command[1])
                command = self.get_input()
            elif command[0] == "print_playlist":
                print(self.playlist)
                command = self.get_input()
            else:
                print("Bad input!")
                command = self.get_input()
        else:
            print("Goodbye!")


def main():
    player = MusicPlayer()
    player.print_messages()
    player.interface()


if __name__ == "__main__":
    main()
