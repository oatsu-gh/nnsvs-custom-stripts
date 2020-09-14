#! /usr/bin/env python3
# coding: utf-8
# Copyright (c) 2020 oatsu
"""
NNSVS用のquestionを生成するやつ
"""
import json


def str_phone_questions(list_all_phonemes, dict_phoneme_classification, mode):
    """
    list_all_phoneme : 全音素のリスト
    dict_phoneme_classification : 音素分類をした辞書のリスト。
    {
     分類名: [音素, 音素, ... ],
     分類名: [音素, ...]
    }
    mode : 'LL', 'L', 'C', 'R', 'RR' のいずれかを選択
    """
    # フルコンテキストラベルから検出するための左右の文字列
    sign_1, sign_2 = {'LL': ('*@', '^*'), 'L': ('*^', '-*'), 'C': ('*-', '+*'),
                      'R': ('*+', '=*'), 'RR': ('*=', '_*')}[mode]

    # 1行分の文字列のリスト。改行文字なし。
    lines = []
    # 音素の分類質問を行に追加
    for key, l_val in dict_phoneme_classification.items():
        # キーの文字列
        s1 = f'"{mode}-Phone_{key}"'
        # 値の文字列
        s2 = '{' + ','.join(f'{sign_1}{ph}{sign_2}' for ph in l_val) + '}'
        # くっつける
        line = ' '.join(('QS', s1, s2))
        # 行のリストに追加
        lines.append(line)
    # 全音素の質問を行に追加
    for ph in list_all_phonemes:
        s1 = f'"{mode}-Phone_{ph}"'
        s2 = '{' + f'{sign_1}{ph}{sign_2}' + '}'
        line = ' '.join(('QS', s1, s2))
        lines.append(line)

    return '\n'.join(lines) + '\n'


def str_fixed_qs_and_cqs():
    """
    音素とは関係なく必ず追加する文字列を返す
    """
    s = (
        # p1
        'QS "C-Phone_Language_Independent_Silence"   {s@*}\n'
        'QS "C-Phone_Language_Independent_Pause"     {p@*}\n'
        'QS "C-Phone_Language_Independent_Break"     {b@*}\n'
        'QS "C-Phone_Language_Independent_Consonant" {c@*}\n'
        'QS "C-Phone_Language_Independent_Vowel"     {v@*}\n'
        # それ以外
        'CQS "p12" {-(\\d+)!}\n'
        'CQS "p13" {!(\\d+)[}\n'
        'CQS "p14" {[(\\d+)$}\n'
        'CQS "p15" {$(\\d+)]}\n'
        'CQS "a1" {/A:(\\d+)-}\n'
        'CQS "a2" {-(\\d+)-}\n'
        'CQS "a3" {-(\\d+)@}\n'
        'CQS "b1" {/B:(\\d+)_}\n'
        'CQS "b2" {_(\\d+)_}\n'
        'CQS "b3" {_(\\d+)@}\n'
        'CQS "c1" {/C:(\\d+)+}\n'
        'CQS "c2" {+(\\d+)+}\n'
        'CQS "c3" {+(\\d+)@}\n'
        'CQS "d1" {/D:(\\NOTE)!}\n'
        'CQS "d2" {!(\\d+)#}\n'
        'CQS "d3" {#(\\d+)$}\n'
        'CQS "d6" {|(\\d+)&}\n'
        'CQS "d7" {&(\\d+);}\n'
        'CQS "d8" {;(\\d+)-}\n'
        'CQS "e1" {/E:(\\NOTE)]}\n'
        'CQS "e2" {](\\d+)^}\n'
        'CQS "e3" {^(\\d+)=}\n'
        'CQS "e6" {!(\\d+)@}\n'
        'CQS "e7" {@(\\d+)#}\n'
        'CQS "e8" {#(\\d+)+}\n'
        'CQS "e26" {|(\\d+)]}\n'
        'CQS "e27" {](\\d+)-}\n'
        'CQS "e57" {~(\\d+)+}\n'
        'CQS "e58" {+(\\d+)!}\n'
        'CQS "f1" {/F:(\\NOTE)#}\n'
        'CQS "f2" {#(\\d+)#}\n'
        'CQS "f3" {#(\\d+)-}\n'
        'CQS "f6" {$(\\d+)+}\n'
        'CQS "f7" {+(\\d+)%}\n'
        'CQS "f8" {%(\\d+);}\n'
    )
    return s


def main():
    with open('config.json', mode='r', encoding='utf-8') as fj:
        d_json = json.load(fj)
    list_all_phonemes = d_json['all_phonemes']
    dict_phoneme_classification = d_json['phoneme_classification']
    s = ''
    s += str_phone_questions(list_all_phonemes, dict_phoneme_classification, mode='L')
    s += str_phone_questions(list_all_phonemes, dict_phoneme_classification, mode='C')
    s += str_phone_questions(list_all_phonemes, dict_phoneme_classification, mode='R')
    s += '\n'
    s += str_fixed_qs_and_cqs()
    with open('result_question_generator.hed', mode='w', encoding='utf-8') as ft:
        ft.write(s)


if __name__ == '__main__':
    main()
