import eyed3
import logging
import os

#   Stupid errors need stupid comments
logging.getLogger("eyed3.mp3.headers").setLevel(logging.CRITICAL)

#   Set path
path = 'media'

#   List directory
files = os.listdir(path)

#   Loop through directory
for root, directories, files in os.walk(path, topdown=False):
    for name in files:

        #   Load mp3 file
        if not name == '.DS_Store':
            audio_file = eyed3.load(os.path.join(root, name))

            #   Variables
            title = audio_file.tag.title
            artist = audio_file.tag.artist
            album = audio_file.tag.album

            if not os.path.isdir(os.path.join(root, artist)):
                os.makedirs(os.path.join(root, artist))
                print(f"Directory '{artist}' didn't exist, making it now.")

            #   Print each file path
            print(f"-------------------------------\n"
                  f"Full Path: {os.path.join(root, name)}.mp3\n"
                  f"Corrected Path: {os.path.join(root, artist, album, title)}.mp3")

        #   TODO
        #   - Conditional function for duplicates
        #   - Conditional function to check if directory exists
        #   - Conditional function to check if 'artist' field is null
        #   - Conditional function to check if 'contributing artist' field is null
