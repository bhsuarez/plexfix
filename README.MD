# PLEXFIX for Google Play Music

I used Google Play Music before it was converted into a YouTube product. After I downloaded my entire library I noticed 
that the folder structure had been lost. All songs had downloaded to this format:

```
Artist - Album 1 - Track 1.mp3
Artist - Album 2 - Track 1.mp3
Artist - Album 2 - Track 2.mp3
```

So I developed a Python script to move the mp3 files into a standard directory structure based on their ID3 information.
I wanted to import my music into Plex, and they recommend the following structure:

```
/Artist
   /Album 1
      Track 1.mp3
   /Album 2
      Track 1.mp3
      Track 2.mp3
```
##  Requirements
*   Windows file system
*   python 3.9 or higher

##  How to use
*   `git clone` this repo
*   Place all mp3 files in a `/media` folder within the root directory
*   Run `python3 main.py`