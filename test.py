"""
This is our first test class and uses the built-in unittest module
You can run these tests by running the following in the terminal
  `python -m unittest test.py`
"""
from unittest import TestCase
from main import MP3Track


class TestMP3Track(TestCase):
    def test_verify_known_fields(self):
        """
        Ensure the fields are properly added to the track upon instantiation
        """
        track = MP3Track("artist", "album", "title")
        self.assertEqual("artist", track.artist)
        self.assertEqual("album", track.album)
        self.assertEqual("title", track.title)

    def test_clean_artist__unknown_artist(self):
        self.assertEqual("Unknown Artist", MP3Track.clean_artist(" "))
        self.assertEqual("Unknown Artist", MP3Track.clean_artist(""))
        self.assertEqual("Unknown Artist", MP3Track.clean_artist(None))

    def test_clean_artist__replace_special_characters(self):
        self.assertEqual("artist", MP3Track.clean_artist("?artist?"))