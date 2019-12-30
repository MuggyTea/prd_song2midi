#!/usr/bin/env python
# -*- coding: utf-8 -*-

from youtube2mp3 import youtube2mp3
from mp4tomp3 import m4a_to_mp3
from chord_analize import detect_chords
from chord2midi import chords2midi
from analize_logging import logger
import ast


class SongToMidi(object):
    def __init__(self):
        pass

    def youtube2midi(self, youtube_url, user_id):
        # youtubeのurlをmp4ファイルにダウンロード
        mp4 = youtube2mp3(youtube_url, user_id)
        # mp4ファイルをmp3に変換
        mp3 = m4a_to_mp3(mp4)
        logger.info("mp3 file: {}".format(mp3))
        # mp3のコード解析
        chord_analyze_str = detect_chords(str(mp3))
        # 辞書型に変換
        chord_analyze_dict = ast.literal_eval(chord_analyze_str)
        logger.info("change type {0} to {1}".format(
            type(chord_analyze_str), type(chord_analyze_dict)))
        # midiファイルに変換
        chords2midi(chord_analyze_dict, user_id)


if __name__ == '__main__':
    youtube_url = "https://www.youtube.com/watch?v=vBmU5v2EyxM"
    user_id = "tesetestestestes"
    song2midi = SongToMidi()
    song2midi.youtube2midi(youtube_url, user_id)
