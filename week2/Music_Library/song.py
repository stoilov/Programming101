class Song:
    MAX_RATING = 5
    MIN_RATING = 0

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.length = length
        self.bitrate = bitrate

    def rate(self, rate_index):
        if rate_index >= Song.MIN_RATING and rate_index <= Song.MAX_RATING:
            self.rating = rate_index
        else:
            error_message = "Rating number must be between {} and {}."
            raise ValueError(error_message.format(Song.MIN_RATING, Song.MAX_RATING))
