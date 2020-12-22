import eyed3
import logging
import os
import shutil
import re

#   Stupid errors need stupid comments
logging.getLogger("eyed3.mp3.headers").setLevel(logging.CRITICAL)

#   Set path
path = 'media'
counter = 0

#   List directory
files = os.listdir(path)


class MP3Track:
    def __init__(self,
                 mp3_artist,
                 mp3_album,
                 mp3_title):

        #   Input validation for / character
        if mp3_title.find("/") != -1:
            mp3_title = mp3_title.replace("/", " AND ")

        self.artist = mp3_artist
        self.album = mp3_album
        self.title = mp3_title

    def __str__(self):
        return f"Artist: {self.artist}" \
               f"Album:  {self.album}" \
               f"Title:  {self.title}"


def create_artist_directory():

    if not os.path.isdir(os.path.join(root, new_mp3_track.artist)):
        os.makedirs(os.path.join(root, new_mp3_track.artist))
        print(f"Directory '{new_mp3_track.artist}' didn't exist, making it now.")


def create_album_directory():

    if not os.path.isdir(os.path.join(root, new_mp3_track.artist, new_mp3_track.album).replace("\\", "/")):
        os.makedirs(os.path.join(root, new_mp3_track.artist, new_mp3_track.album).replace("\\", "/"))
        return f"Directory '{new_mp3_track.artist} / {new_mp3_track.album}' didn't exist, making it now."


#   OS Walk through path
for root, directories, files in os.walk(path, topdown=False):

    #   Loop through files
    for name in files:

        if name.endswith('mp3'):
            #   Load MP3 file
            audio_file = eyed3.load(os.path.join(root, name))

            #   Increment counter
            counter += 1

            #   Set Variables
            new_mp3_track = MP3Track(audio_file.tag.artist, audio_file.tag.album, audio_file.tag.title)
            print(f"Loaded {new_mp3_track}")

            #   Artist null check
            if new_mp3_track.artist == ' ' or new_mp3_track.artist == '' or new_mp3_track.artist is None:
                new_mp3_track.artist = "Unknown Artist"

            #   If Artist ID3 name contains a /, replace with &
            if new_mp3_track.artist.find("/") != -1:
                new_mp3_track.artist = new_mp3_track.artist.replace("/", "&")

            #   Album null check
            if new_mp3_track.album == ' ' or new_mp3_track.album == ' ' or new_mp3_track.album is None:
                new_mp3_track.album = "Unknown Album"

            #   Set files and directories
            original_path = os.path.join(root, name)
            destination_path = os.path.join(root, new_mp3_track.artist, new_mp3_track.album, new_mp3_track.title) + ".mp3 "

            #   Get Size
            size = str(os.path.getsize(original_path))

            #   Create album directory if it doesn't exist
            create_artist_directory()

            #   Create artist directory if it doesn't exist
            create_album_directory()

            #   Move file
            shutil.move(original_path, destination_path)

            #   Print out
            print(f"Moved {original_path} to {destination_path} size: {size}")

print(f"Total songs moved: {counter}")


def __main__():
    return "Hello world"



