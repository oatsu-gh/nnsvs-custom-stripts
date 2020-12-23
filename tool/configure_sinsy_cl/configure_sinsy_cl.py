#!/usr/bin/env python3
# Copyright (c) 2020 oatsu
"""
sinsyのラベルだとclの直前の音素の長さが0なので何とかする。
"""

import utaupy as up
from glob import glob
from os.path import dirname, basename
from os import makedirs
from pprint import pprint

def distribute_time(label):
    """
    長さ0の音素が出現したとき、次の音素の音素長を分配する。
    """
    l_temp = []
    for phoneme in label:
        duration = phoneme.end - phoneme.start
        # 時間が0のとき
        if duration == 0:
            l_temp.append(phoneme)
        # 時間が0じゃないけど、0のストックがあるとき
        elif duration > 0 and len(l_temp) > 0:
            print('hit!')
            l_temp.append(phoneme)
            new_duration = duration // len(l_temp)
            for i, ph in enumerate(l_temp[1:], 1):
                print(str(ph))
                ph.start = l_temp[i-1].start + new_duration
                print(str(ph))

            l_temp = []
        elif duration > 0 and len(l_temp) == 0:
            continue
        else:
            raise Exception(f'duration: {duration}, len(l_temp): {len(l_temp)}')
    label.reload()


def main():
    path_label_dir = input('path_label_dir: ').strip('"')
    labels = glob(f'{path_label_dir}/**/*.lab', recursive=True)
    for path in labels:
        print(path)
        label = up.label.load(path)
        distribute_time(label)
        makedirs(f'out/{basename(dirname(path))}', exist_ok=True)
        label.write(f'out/{basename(dirname(path))}/{basename(path)}')

if __name__ == '__main__':
    main()
