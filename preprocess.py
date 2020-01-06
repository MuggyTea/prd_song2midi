#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
音響解析の前処理をするための関数
・長波打楽器分離(HPSS)
・定Q変換を行う
"""

import librosa
import numpy as np
import matplotlib.pyplot as plt
import pydub


class PreProcess(object):

    def __init__(self, file_path):
        # main functions
        self.sr = 16000
        # self.margin = 1.5
        # self.offset = 116
        # self.duration = 20
        self.file_path = file_path

    def hpss(self):
        """
        打楽器分離
        """
        song, sr = librosa.load(self.file_path, sr=self.sr)
        song_harm, song_perc = librosa.effects.hpss(song)

        # ファイル書き出し
        librosa.output.write_wav("{}_org.wav".format(file_path), song, sr)
        librosa.output.write_wav(
            "{}_hpss_harm.wav".format(file_path), song_harm, sr)
        librosa.output.write_wav(
            "{}_hpss_perc.wav".format(file_path), song_perc, sr)
        # mp3ファイルに変換
        sound = pydub.AudioSegment.from_wav(
            "{}_hpss_harm.wav".format(file_path))
        sound.export("harm_{}".format(file_path), format="mp3")

        return song_harm, song_perc

    def cqt(self):
        y, sr = librosa.load(self.file_path, sr=self.sr)
        n_bins = 84
        hop_length = 1024
        constant_q = librosa.cqt(
            y=y, sr=sr)
        cqt_pitch = np.abs(constant_q)
        print(cqt_pitch)
        print(type(cqt_pitch))
        # inverse CQT
        y = librosa.core.icqt(C=cqt_pitch)
        # ファイル書き出し
        librosa.output.write_wav(
            "{}_cqt.wav".format(self.file_path), y, sr=sr)
        # クロマ特徴抽出
        chroma = librosa.feature.chroma_cqt(C=cqt_pitch, sr=self.sr)
        return chroma

    def chroma(self, cqt_pitch):
        print(cqt_pitch)
        print(type(cqt_pitch))
        # wav_data = np.ndarray(cqt_pitch)
        # ファイル書き出し
        filepath = "{}_chroma.wav".format(self.file_path)
        print(filepath)
        librosa.output.write_wav(
            filepath, y=np.asfortranarray(cqt_pitch), sr=self.sr)
        # mp3ファイルに変換
        sound = pydub.AudioSegment.from_wav(str(filepath))
        sound.export("chroma_{}.mp3".format(self.file_path), format="mp3")


if __name__ == "__main__":
    file_path = "tmp/catchTheStar.mp3"
    preprocess = PreProcess(file_path)
    # 打楽器分離
    # song_harm, song_perc = preprocess.hpss()
    # 定Q変換
    cqt_pitch = preprocess.cqt()
    # クロマ特徴
    # preprocess.chroma(cqt_pitch)
