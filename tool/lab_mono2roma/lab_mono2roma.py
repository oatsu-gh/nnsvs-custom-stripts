#! /usr/bin/env python3
# coding: utf-8
# Copyright (c) 2020 oatsu
"""
モノフォンラベルをローマ字CVラベルに変換する。
UTAU連続音の思想のラベリングにより、滑らかな発声の歌声モデル構築を目指す。

動作モード
- 子音の開始位置を発声開始位置にする。（オーバーラップ終了時刻の思想）←こっちを実装した。
- 子音と母音の区切り位置を発声開始位置にする（先行発声終了時刻の思想）
"""

import json
from datetime import datetime
from glob import glob
from os import makedirs
from os.path import basename, isfile, splitext

import utaupy as up


def monolabel_to_intermediate(mono_label, d_phoneme_category):
    """
    モノフォンラベルをいったん2次元リストにする
    [[子音のラベル, 母音のラベル], [子音のラベル, 母音のラベル], [母音のラベル], ...]
    """
    # 子音一覧のリスト
    consonants = d_phoneme_category['consonants']
    # 母音一覧のリスト
    vowels = d_phoneme_category['vowels']
    # [[子音のラベル, 母音のラベル], [子音のラベル, 母音のラベル], [母音のラベル], ...]
    l_temp_2d = []
    # [子音のラベル, 母音のラベル]
    l_temp_inner = []
    for mono_phoneme in mono_label:
        if mono_phoneme.symbol in consonants:
            l_temp_inner.append(mono_phoneme)
        elif mono_phoneme.symbol in vowels:
            l_temp_inner.append(mono_phoneme)
            l_temp_2d.append(l_temp_inner)
            l_temp_inner = []
        else:
            l_temp_inner.append(mono_phoneme)
            l_temp_2d.append(l_temp_inner)
            l_temp_inner = []
    return l_temp_2d


def intermadiate_to_romalabel(intermadiate_2dlist, base='consonant'):
    """
    intermadiate_2dlist:
        [[子音のラベル, 母音のラベル], [子音のラベル, 母音のラベル], [母音のラベル], ...]
    return:
        [CVラベル, CVラベル, CVラベル, ...]
    """
    base_idx = {'consonant': 0, 'vowel': -1}[base]
    roma_label = up.label.Label()
    for inner_list in intermadiate_2dlist:
        roma_phoneme = up.label.Phoneme()
        roma_phoneme.start = inner_list[base_idx].start
        roma_phoneme.end = inner_list[-1].end
        roma_phoneme.symbol = ''.join(ph.symbol for ph in inner_list)
        roma_label.append(roma_phoneme)
    return roma_label


def uppercase_to_lowercase(label: up.label.Label):
    """
    無声化の母音を小文字に戻す。
    hedを作るのが楽になる。
    """
    translation_table = str.maketrans('AIUEO', 'aiueo')
    for phoneme in label:
        phoneme.symbol = phoneme.symbol.translate(translation_table)


def main():
    """
    ファイル入出力のパスを指定する。
    """
    with open('./config.json', 'r') as f:
        config = json.load(f)
    d_phoneme_category = config['phoneme_category']

    # 変換元のモノフォンラベルのパスを入力させる
    path_input = input('Input path of mono-label directory\n>>> ')
    if isfile(path_input):
        path_mono_label_files = [path_input]
    else:
        path_mono_label_files = glob(f'{path_input}/**/*.lab', recursive=True)

    now = datetime.now().strftime('%Y%m%d_%H%M%S')
    makedirs(f'out/{now}', exist_ok=True)
    # モノフォンラベルをかなラベルにする。
    for path_mono_label in path_mono_label_files:
        print(f'  {path_mono_label}')
        # 変換元のモノフォンラベル
        mono_label = up.label.load(path_mono_label)
        # いったん中間フォーマットとして二次元リストにする
        intermadiate = monolabel_to_intermediate(mono_label, d_phoneme_category)
        # 変換先のかな文字ラベル
        roma_label = intermadiate_to_romalabel(intermadiate)
        # 母音無性化を無効にする
        uppercase_to_lowercase(roma_label)
        # ファイル出力
        path_roma_label = f'out/{now}/{basename(path_mono_label)}'
        roma_label.write(path_roma_label)


if __name__ == '__main__':
    main()
    input('Press Enter to exit.')
