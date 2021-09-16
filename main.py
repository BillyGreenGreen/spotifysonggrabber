from SwSpotify import spotify
import time

while True:
    time.sleep(3)
    try:
        with open("song.txt", "w+") as f:
            line = f.readline()
            song = spotify.artist() + " - " + spotify.song()
            if len(song) > 42:
                sub = len(song) - 42
                song = song[:-sub] + "..."
            print(line)
            print(song)
            if line != song:
                f.write(song)
                f.close()

    except:
        with open("song.txt", "w") as f:
            f.write("No song currently playing...")
            f.close()