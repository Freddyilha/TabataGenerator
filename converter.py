from pydub import AudioSegment
from pydub.playback import play

class Converter:
    def generate(self):

        twenty_seconds = 20 * 1000

        ten_seconds = 10 * 1000

        track = AudioSegment.from_file("Songs/Track-1.mp3", "mp3")

        countdown = AudioSegment.from_file("Songs/Five-seconds-countdown.mp3", "mp3")

        track_duration = len(track)

        timestamps = [0,twenty_seconds]

        for index,timestamp in enumerate(range(0, track_duration, twenty_seconds+ten_seconds)):
            if index % 2 == 0:
                timestamps.append(timestamps[-1] + ten_seconds)
            else:
                timestamps.append(timestamps[-1] + twenty_seconds)

        for index,timestamp in enumerate(timestamps):
            if index == 0:
                final_track = track[timestamps[index] : timestamps[index+1]-5000] + (track[timestamps[index+1]-5000 : timestamps[index+1]]).overlay(countdown)
            else:
                if index == 1:
                    continue
                if index % 2 == 1:
                    final_track = final_track + track[timestamps[index-1] : timestamps[index]-5000] + (track[timestamps[index]-5000 : timestamps[index]]).overlay(countdown)
                else:
                    final_track = final_track + (track[timestamps[index-1] : timestamps[index]-5000] - 10) + (track[timestamps[index]-5000 : timestamps[index]] - 10).overlay(countdown)

        final_track.export("TabataSongs/Tabatified-lower-norfair.mp3", format="mp3")


if __name__ == '__main__':
    converter = Converter()

    converter.generate()
