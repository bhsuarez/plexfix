import eyed3
import logging
import os

#   Stupid error
logging.getLogger("eyed3.mp3.headers").setLevel(logging.CRITICAL)

#   Set path
path = 'media'

#   List directory
files = os.listdir(path)

#   Loop through directory
for root, directories, files in os.walk(path, topdown=False):
    for name in files:

        #   Load mp3 file
        audio_file = eyed3.load(os.path.join(root, name))

        #   Variables
        title = audio_file.tag.title
        artist = audio_file.tag.artist
        album = audio_file.tag.album

        #   Print each file path
        print(f"Full Path: {os.path.join(root, artist, album, title)}.mp3")
