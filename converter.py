import os
from pydub import AudioSegment
from pydub.playback import play

def main():

    track = AudioSegment.from_file("Songs/Track-1.mp3", "mp3")

    play(track)


if __name__ == '__main__':
    main()
