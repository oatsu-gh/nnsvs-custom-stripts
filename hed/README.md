# conf

学習パターンを制御するための、音素や楽譜情報の分類ファイル。

どれか1つのファイルを使って学習させます。

## hed を作るときの注意

- d1, e1, f1 はCQSの最初に置かないといけない。

## ファイル比較

いずれも kiritan-singing および sinsy のjp_qst001.hed （2020年10月以前のもの）を改造したもの。

---

### 2020年11月以降のファイル

#### jp_qst_crazy_mono_001.hed

- 184次元

- 2020-11-04 作成、2020-11-15修正
- 強弱記号：**すべて無視**
- 拍子情報：無視
- 母音無性化：**対応**（通常母音と同一視）
- 音素フラグを無視
- question の名前を一部整理

##### e57, e58 を変更

変更前

```
CQS "e57" {~(\d+)+}
CQS "e58" {+(\d+)!}
```

変更後

```
CQS "e57" {~([pm]\d+)+}
CQS "e58" {+([pm]\d+)!}
```

#### jp_qst_crazy_mono_002.hed

- 192次元
- 2020年11月15日作成
- 001から派生、**フレーズ内ノート数**（e18 - e25）を取得するようにした。
- 母音無性化：区別せず同一視

#### jp_qst_crazy_mono_002-2.hed

- 183次元
- 2020年11月15日作成
- 002から派生。"JPN"などの**言語情報を無効化**（a4, b4, c4）
- 母音無性化：区別せず同一視

#### jp_qst_crazy_mono_003.hed

- 178次元
- 2020年11月15日作成
- 002-2 から派生
- スラー情報を無効化（e26, e27）
- ノート長を拍数でカウントするのを無効化（d8, e8, f8）
  - タイミング音痴になりました。

#### jp_qst_crazy_mono_004.hed（予定）

- 184次元
- 2020年11月16日作成
- **BPM**をCQS取得（d5, e5, f5）
- ノート長を拍数でカウントするのを復活（d8, e8, f8）
- スラー情報は無効のまま

#### jp_qst_crazy_mono_005_173D.hed

- 173次元
- 2020-11-16
- 004から派生、simple_4-4に近くなった。
- d5, e5, f5 なし
- d6, e6, f6 あり
- e18 - e25 なし

#### jp_qst_crazy_mono_005-2_185D.hed

- 185次元
- 2020-11-23
- 005から派生、jp_qst001_nnsvs.hed を参考に母音のグループ化を追加。

#### jp_qst_crazy_mono_005-2_enunu_182D.hed

- 182次元
- 2020-11-24
- 005-2から派生、ENUENU用の仕様。普通に使ってもよさそう。
- スケール情報無効化（d3, e3, f3）

### jp_qst_crazy_mono_006_193D.hed

- 193次元
- 2020-12-09
- 005-2から派生
- ノートのフレーズ内位置のコンテキストを復活
- 母音のグループ化あり
- 各種キー名を整理

### jp_qst_crazy_mono_006-2_181D.hed

- 193次元
- 2020-12-09
- 005-2から派生
- ノートのフレーズ内位置のコンテキストを復活
- 母音のグループ化**なし**
- **silとpauのグループを削除**
- 各種キー名を整理

### jp_qst_crazy_roma_002_627D.hed

- 627次元
- 2020-12-22
- 006-2から派生
- ローマ字CV音素表記用

### jp_qst_crazy_roma_002-2_595D.hed

- 595次元
- 2020-12-23
- roma_002から派生
- ローマ字CV音素表記用
- L-Phone の子音グループを削除
- R-Phone の母音グループを削除

---

### 2020年10月以前のファイル

#### jp_qst001_nnsvs_simple_4.hed

- 285次元
- 強弱記号：**取得**
- 拍子情報：無視
- 有声子音と無声子音：区別あり
- 母音無声化：対応
- 下記動画投稿時に使用していたファイルです。
  - [【AIおにくる】きみも悪い人でよかった【NNSVSカバー】 - ニコニコ動画](https://www.nicovideo.jp/watch/sm37452833 https://www.nicovideo.jp/watch/sm37452833)

#### jp_qst001_nnsvs_simple_4-2.hed

- 282次元
- N_is_n の項目を削除

#### jp_qst001_nnsvs_simple_4-3.hed

- 285次元
- N_is_n の項目あり
- Yuusei_Shiin から N を削除
  - simple_4 が r と N を混同して学習するのを対策したい。
- 2020年10月09日 作成

#### jp_qst001_nnsvs_simple_4-4.hed

- 279次元
- N_is_n なし
- Boin_and_N を削除
  - N か n か知らないけど、r などの周辺で勝手に登場するのを対策したい。
- 2020年10月19日作成

#### jp_qst001_nnsvs_simple_5.hed

- 217次元
- 強弱記号：無視
- 拍子情報：無視
- 有声子音と無声子音：区別あり
- 母音無声化：対応

### jp_qst001_nnsvs_simple_6_LLRR.hed

- ???次元
- **2つ前の音素(p2) および 2つ後の音素(p4) を扱える。**
  - ステップ1の処理で jp_qst001_nnsvs_simple_5.hed の8倍くらい時間がかかるので注意。
- 強弱記号：無視
- 拍子情報：無視
- 有声子音と無声子音：区別あり
- 母音の無声化：**非対応**

#### jp_qst001_nnsvs_simple_6_LL_noAIUEO.hed

- 228次元
- **2つ前の音素(p2) および 2つ後の音素(p4) を扱える。**
  - ステップ1の処理で jp_qst001_nnsvs_simple_5.hed の8倍くらい時間がかかるので注意。
- 強弱記号：無視
- 拍子情報：無視
- 有声子音と無声子音の区別あり
- 母音の無声化：**非対応**
-
#### jp_qst001_nnsvs_simple_6_LLRR_noAIUEO.hed

- 275次元
- **2つ前の音素(p2) および 2つ後の音素(p4) を扱える。**
  - ステップ1の処理で jp_qst001_nnsvs_simple_5.hed の8倍くらい時間がかかるので注意。
- 強弱記号：無視
- 拍子情報：無視
- 有声子音と無声子音の区別あり
- 母音の無声化：**非対応**

#### jp_qst_crazy_roma_001.hed
- 447次元
- **ローマ字CV音素用**
- 現在の音素と、前後1音素ずつのみ取得
- 直前の音素は母音で分類
- 強弱記号：無視
- 拍子情報：無視
- 母音の無声化：**非対応**
- 子音と母音の距離 (p14, p15) を無効化
