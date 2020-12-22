import eyed3
import logging
import os
import shutil

#   Stupid errors need stupid comments
logging.getLogger("eyed3.mp3.headers").setLevel(logging.CRITICAL)

#   Set path
path = 'media'
counter = 0

#   List directory
files = os.listdir(path)

#   OS Walk through path
for root, directories, files in os.walk(path, topdown=False):

    #   Loop through files
    for name in files:

        if name.endswith('mp3'):
            #   Load MP3 file
            audio_file = eyed3.load(os.path.join(root, name))
            counter += 1

            #   Set Variables
            title = audio_file.tag.title
            artist = audio_file.tag.artist
            #   Null check
            if artist == ' ' or artist == '' or artist is None:
                artist = "Unknown Artist"
            #   If the artist ID3 name contains a /, replace with &
            if artist.find("/") != -1:
                artist = artist.replace("/", "&")

            album = audio_file.tag.album

            #   If the album is null
            if album == ' ' or album == '' or album is None:
                album = "Unknown Album"

            #   Files
            original_path = os.path.join(root, name)
            destination_path = os.path.join(root, artist, album, title) + ".mp3"

            #   Get Size
            size = str(os.path.getsize(original_path))

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

            #   Print out
            print(f"Moved {original_path} to {destination_path} size: {size}")

print(f"Total songs moved: {counter}")