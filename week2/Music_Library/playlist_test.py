import unittest
from playlist import Playlist
from song import Song


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist("Led Zeppelin")

    def test_playlist_init(self):
        self.assertEqual(self.playlist.name, "Led Zeppelin")
        self.assertListEqual(self.playlist.songs, [])

    def test_add_song(self):
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            5,
            334,
            320000
        )
        self.playlist.add_song(song)
        self.assertEqual(self.playlist.songs[0], song)

    def test_remove_song(self):
        song_name = "Whole Lotta Love"
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            5,
            334,
            320000
        )
        self.playlist.add_song(song)
        self.playlist.remove_song(song_name)
        songs_with_this_name = 0
        for song in self.playlist.songs:
            if song.title == song_name:
                songs_with_this_name += 1
        self.assertEqual(songs_with_this_name, 0)

    def test_remove_song_more_than_one(self):
        song_name = "Whole Lotta Love"
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            5,
            334,
            320000
        )
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        self.playlist.remove_song(song_name)
        songs_with_this_name = 0
        for song in self.playlist.songs:
            if song.title == song_name:
                songs_with_this_name += 1
        self.assertEqual(songs_with_this_name, 0)

    def test_total_length(self):
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            5,
            334,
            320000
        )
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        length = self.playlist.total_length()
        self.assertEqual(length, "16:42")

    def test_remove_disrated(self):
        rating = 4
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            3,
            334,
            320000
        )
        self.playlist.add_song(song)
        self.playlist.remove_disrated(rating)
        songs_with_this_rate = 0
        for song in self.playlist.songs:
            if song.rating < rating:
                songs_with_this_rate += 1
        self.assertEqual(songs_with_this_rate, 0)

    def test_remove_disrated_more_than_one(self):
        rating = 4
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            3,
            334,
            320000
        )
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        self.playlist.remove_disrated(rating)
        songs_with_this_rate = 0
        for song in self.playlist.songs:
            if song.rating < rating:
                songs_with_this_rate += 1
        self.assertEqual(songs_with_this_rate, 0)


    def test_remove_bad_quality(self):
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            3,
            334,
            240000
        )
        self.playlist.add_song(song)
        self.playlist.remove_bad_quality()
        songs_with_this_rate = 0
        for song in self.playlist.songs:
            if song.bitrate < 320000:
                songs_with_this_rate += 1
        self.assertEqual(songs_with_this_rate, 0)

    def test_remove_bad_quality_more_than_one(self):
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            3,
            334,
            240000
        )
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        self.playlist.remove_bad_quality()
        songs_with_this_rate = 0
        for song in self.playlist.songs:
            if song.bitrate < 320000:
                songs_with_this_rate += 1
        self.assertEqual(songs_with_this_rate, 0)

    def test_show_artists(self):
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            5,
            334,
            320000
        )
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        artists = self.playlist.show_artists()
        self.assertSetEqual(artists, {"Led Zeppelin"})

    def test_playlist_str(self):
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            5,
            334,
            320000
        )
        self.playlist.add_song(song)
        string_repr = self.playlist.__str__()
        self.assertEqual(string_repr, "Led Zeppelin Whole Lotta Love - 5:34")

    def test_playlist_str_more_songs(self):
        song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            5,
            334,
            320000
        )
        self.playlist.add_song(song)
        self.playlist.add_song(song)
        string_repr = self.playlist.__str__()
        self.assertEqual(string_repr, "Led Zeppelin Whole Lotta Love - 5:34\nLed Zeppelin Whole Lotta Love - 5:34")

if __name__ == '__main__':
    unittest.main()
