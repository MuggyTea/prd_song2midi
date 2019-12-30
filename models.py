#!/usr/bin/env python
# -*- coding: utf-8 -*-

from youtube2mp3 import youtube2mp3
from mp4tomp3 import m4a_to_mp3
from chord_analize import detect_chords
from chord2midi import chords2midi


class SongToMidi(object):
    def __init__(self):
        pass

    def youtube2midi(self, youtube_url, user_id):
        # youtubeのurlをmp4ファイルにダウンロード
        mp4 = youtube2mp3(youtube_url, user_id)
        # mp4ファイルをmp3に変換
        mp3 = m4a_to_mp3(mp4)
        # mp3のコード解析
        chord_analize_dict = detect_chords(mp3)
        # midiファイルに変換
        chords2midi(chord_analize_dict, user_id)


if __name__ == '__main__':
    youtube_url = "https://youtu.be/Xnws-1Oz4kM"
    user_id = "tesetestestestes"
    song2midi = SongToMidi()
    song2midi.youtube2midi(youtube_url, user_id)
