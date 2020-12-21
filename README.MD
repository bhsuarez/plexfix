# PLEXFIX

A Python script to move files into the standard Plex music structure based on ID3 information.

from
```
Artist - Album 1 - Track 1.mp3
Artist - Album 2 - Track 1.mp3
Artist - Album 2 - Track 2.mp3
```
to
```
/Artist
   /Album 1
      Track 1.mp3
   /Album 2
      Track 1.mp3
      Track 2.mp3
```

##  TODO
- [DONE] Conditional replace for '/' in 'artist' field with '&' character
- [DONE] Conditional function to check if artist/album directory exists
- [DONE] Conditional function to check if 'artist' field is null
- Conditional function to check if 'contributing artist' field is null
- Conditional function for finding and moving duplicate MP3 files
