from pydub import AudioSegment
from pydub.playback import play

class Converter:
    def generate(self):

        twentyfive_seconds = 25 * 1000

        fifthteen_seconds = 15 * 1000

        track = AudioSegment.from_file("Songs/Track-1.mp3", "mp3")

        countdown = AudioSegment.from_file("Songs/Five-seconds-countdown.mp3", "mp3")

        track_duration = len(track)

        rest_countdown = [timestamp for timestamp in range(0, track_duration, twentyfive_seconds)] 

        exercices_countdown = [timestamp for timestamp in range(0, track_duration, fifthteen_seconds)] 

        track_start = track[:20000]
        rest_of_song = track[20*1000:]

        track_start = track_start.append(countdown, crossfade=(4126))
        
        play(track_start)

        # return [rest_countdown, exercices_countdown]

if __name__ == '__main__':
    converter = Converter()

    converter.generate()
