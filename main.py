import eyed3
import logging
import os
import shutil

#   Stupid errors need stupid comments
logging.getLogger("eyed3.mp3.headers").setLevel(logging.CRITICAL)

#   Set path
path = 'media'

#   List directory
files = os.listdir(path)

#   Loop through directory
for root, directories, files in os.walk(path, topdown=False):
    for name in files:

        #   Load MP3 file
        if not name == '.DS_Store':
            audio_file = eyed3.load(os.path.join(root, name))

            #   Variables
            title = audio_file.tag.title
            artist = audio_file.tag.artist
            #   If the artist ID3 name contains a /, replace with &
            if artist.find("/") != -1:
                artist = artist.replace("/", "&")
            album = audio_file.tag.album

            #   Files
            original_path = os.path.join(root, name)
            destination_path = os.path.join(root, artist, album, title)+".mp3"

            #   Create artist directory if it doesn't exist
            if not os.path.isdir(os.path.join(root, artist)):
                os.makedirs(os.path.join(root, artist))
                print(f"Directory '{artist}' didn't exist, making it now.")

            #   Create album directory if it doesn't exist
            if not os.path.isdir(os.path.join(root, artist, album)):
                os.makedirs(os.path.join(root, artist, album))
                print(f"Directory '{artist} / {album}' didn't exist, making it now.")

            #   Move file
            shutil.move(original_path, destination_path)

            #   Print each file path
            print(f"-------------------------------\n"
                  f"Original Path: {original_path}\n"
                  f"Corrected Path: {destination_path}")
