from pydub import AudioSegment
from pydub.playback import play

class Converter:
    def generate(self):

        ten_seconds = 10 * 1000

        track = AudioSegment.from_file("Songs/Track-1.mp3", "mp3")

        track_duration = len(track)

        countdown_starts = [timestamp for timestamp in range(0, track_duration, ten_seconds)] 

        print(countdown_starts)

        # play(track)


if __name__ == '__main__':
    converter = Converter()

    converter.generate()
