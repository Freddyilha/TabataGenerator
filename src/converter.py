import os
from pydub import AudioSegment
from pydub.playback import play

track = AudioSegment.from_file("Countdown.mp3", "mp3")

play(track)

# print("banana")
