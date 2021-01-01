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

#   Illegal characters array
sp_chars = [';', ':', '!', "*", "/", "|", '"', "<", ">", "&", "?"]

#   Cleanup function
#   cleanup.cleanup_directory()


class MP3Track:
    def __init__(self,
                 mp3_artist,
                 mp3_album,
                 mp3_title):

        #   Input validation for artist
        if mp3_artist == ' ' or mp3_artist == '' or mp3_artist is None:
            mp3_artist = "Unknown Artist"
        for i in sp_chars:
            mp3_artist = mp3_artist.replace(i, "")
        mp3_artist = mp3_artist.strip()

        #   Input validation for album
        if mp3_album == ' ' or mp3_album == '' or mp3_album is None:
            mp3_album = "Unknown Album"
        for i in sp_chars:
            mp3_album = mp3_album.replace(i, "")
        mp3_album = mp3_album.strip()

        #   Input validation for title
        for i in sp_chars:
            mp3_title = mp3_title.replace(i, "")
        mp3_title = mp3_title.strip()

        #   Setters for object
        self.artist = mp3_artist
        self.album = mp3_album
        self.title = mp3_title

    def __str__(self):
        return f"\n" \
               f"Artist: {self.artist}\n" \
               f"Album:  {self.album}\n" \
               f"Title:  {self.title}\n"


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

            #   Set files and directories
            original_path = os.path.join(root, name)
            destination_path = os.path.join(root, new_mp3_track.artist, new_mp3_track.album,
                                            new_mp3_track.title) + ".mp3"

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
        else:
            print("Error: wrong file format")

print(f"Total songs moved: {counter}")


def __main__():
    return "Hello world"
