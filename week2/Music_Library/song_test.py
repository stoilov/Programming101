import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song(
            "Whole Lotta Love",
            "Led Zeppelin",
            "Led Zeppelin II",
            5,
            334,
            320000
        )

    def test_song_init(self):
        self.assertEqual(self.song.title, "Whole Lotta Love")
        self.assertEqual(self.song.artist, "Led Zeppelin")
        self.assertEqual(self.song.album, "Led Zeppelin II")
        self.assertEqual(self.song.rating, 5)
        self.assertEqual(self.song.length, 334)
        self.assertEqual(self.song.bitrate, 320000)

    def test_rate(self):
        self.song.rate(4)
        self.assertEqual(self.song.rating, 4)

    def test_rate_error(self):
        with self.assertRaises(ValueError):
            self.song.rate(200000)

if __name__ == '__main__':
    unittest.main()
