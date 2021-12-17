from pydub import AudioSegment
from pydub.playback import play

class Converter:
    def generate(self):

        five_seconds = 5 * 1000

        ten_seconds = 10 * 1000

        fifteen_seconds = 15 * 1000

        twenty_seconds = 20 * 1000

        track = AudioSegment.from_file("Songs/Song_name.mp3", "mp3")

        countdown = AudioSegment.from_file("Songs/Five-seconds-countdown.mp3", "mp3")

        track_duration = len(track)

        rest_timestamps = [fifteen_seconds]

        while rest_timestamps[-1] < track_duration:

            if len(rest_timestamps) % 2 == 1:
                rest_timestamps.append(rest_timestamps[-1] + ten_seconds)
            else:
                rest_timestamps.append(rest_timestamps[-1] + twenty_seconds)

        if rest_timestamps[-1] > track_duration:
            rest_timestamps.pop()

        start_timestamps = [timestamp+five_seconds for timestamp in rest_timestamps]

        if start_timestamps[-1] > track_duration:
            start_timestamps.pop()

        for index, (rest, start) in enumerate(zip(rest_timestamps, start_timestamps)):

            if index == 0:
                final_track = track[0 : rest_timestamps[index]] + (track[rest_timestamps[index] : start_timestamps[index]]).overlay(countdown + 10)
            else:
                if index % 2 == 1:
                    final_track = final_track + (track[start_timestamps[index-1] : rest_timestamps[index]] - 10) + (track[rest_timestamps[index] : start_timestamps[index]] - 10).overlay(countdown + 10)
                else:
                    final_track = final_track + track[start_timestamps[index-1] : rest_timestamps[index]] + (track[rest_timestamps[index] : start_timestamps[index]]).overlay(countdown + 10)

        final_track.export("TabataSongs/Tabatified-Song_name.mp3", format="mp3")

if __name__ == '__main__':
    converter = Converter()

    converter.generate()
