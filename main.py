import eyed3
import logging
import os
logging.getLogger("eyed3.mp3.headers").setLevel(logging.CRITICAL)

path = 'media'

files = os.listdir(path)

for root, files in os.walk(path, topdown=False):
    for name in files:
        audio_file = eyed3.load(os.path.join(root, name))

        # Variables
        title = audio_file.tag.title
        artist = audio_file.tag.artist
        album = audio_file.tag.album

        # print(f"{audio_file.tag.artist} / {audio_file.tag.album} / {audio_file.tag.title}")
        print(f"Full Path: {os.path.join(root, artist, album, title)}.mp3")
