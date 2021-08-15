# MogiCasher
![Current version](https://img.shields.io/badge/MogiCasher-1.5.1-red)
![Python version](https://img.shields.io/badge/Python-3.9.6-blue)
![PySimpleGUI version](https://img.shields.io/badge/PySimpleGUI-4.45.0-orange)
![pandas version](https://img.shields.io/badge/pandas-1.3.1-green)

Readmeにようこそ！

**いろんなことが適当に書いてあります！！！**

## 目次
1. [概要](/README.md#概要)
   - [機能](/README.md#機能)
   - [動作環境](/README.md#動作環境)
   - [CSVファイルの形式](/README.md#CSVファイルの形式)
   - [対応コード](/README.md#対応コード)
   - [ファイル構成](/README.md#ファイル構成)
1. [使い方](/README.md#使い方)
   - [基本操作](/README.md#基本操作)
     - [下準備](/README.md#下準備)
     - [起動](/README.md#起動)
     - [コードデータを読み込む](/README.md#コードデータを読み込む)
     - [コードを読み取る](/README.md#コードを読み取る)
     - [精算する](/README.md#精算する)
     - [ソフトを終了する](/README.md#ソフトを終了する)
   - [その他](/README.md#その他)
     - [Analyze](/README.md#Analyze)
     - [Setting](/README.md#Setting)
1. [注意事項](/README.md#注意事項)
1. [解説](/README.md#解説)
   - [リスト](/README.md#リスト)
   - [バーコード読み取り時](README.md#バーコード読み取り時)

## 概要
### 機能
**CSVファイルとlistオブジェクトを使用するシンプルなソフトです。**  
*なんでコードがやたら長いのかって? UIの挙動を謎に作りこんだからだよ*
- 概ねレジとして機能するソフトです。実際のレジのように使えます。
- 各品目のコード、値段、売上個数が書かれたCSVファイルを読み込みます。
- CSVデータをもとにした一覧表と現在の売り上げを表示します。
- 終了時にその時点での売り上げデータを自動で保存します。
- 日本語でいい感じのフォントがないので仕方なく英語にしました。

### 動作環境
Python3のソフトです。  
以下の外部ライブラリがインストールされているコンピューターで動作します。(はず)
- ライブラリ
  - datetime
  - glob
  - os
  - subprocess
  - [pandas](https://pandas.pydata.org/)
  - [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)
  - webbrowser

- **アプリケーション化した場合**
  - casher.pyをアプリケーション化してください。
  - pyinstallerを使用してexe化した場合、Windows10では動作します。
  - セキュリティソフトの設定によってはブロックされる場合があります。
  - 8以前のWindowsやMacOSではよくわかりません。

### CSVファイルの形式
- UI的には5品目を想定していますが、**何品目でも対応可能です。**
- 名前は *profile.csv* にしてください。ただし前後には何を入れてもOKです。 ex.) profile_0806.csv
- ~~CSVのカラムは、コードの列を除き指定はありません。コードの列のみ"***CODE***"にしてください。~~　　
- CSVのカラムはどの列も指定はありません。
- また、下では1列目が#~の連番ですが、仕様上**どんな文字列にしても問題ありません。**
  - ※英語フォントなのでアルファベット以外は表示がダサくなります。

| (tag) | CODE | PRICE | UNITS |
| --: | -------------: | ---: | ---: |
| #1 | xxxxxxxx | xxx | 0 |
| #2 | xxxxxxxx | xxx | 0 |
| ... | ... | ... | ... |
| #5 | xxxxxxxx | xxx | 0 |

### 対応コード

EAN(JAN)8桁を想定していますが、バーコードリーダーが読み取れる形式すべてに対応しています。

### ファイル構成
このソフトのファイル構成です。
DLする際はmogicasherディレクトリごとDLするのがお勧めです。

    dist
    ┗ mogicasher
      ┗ interface
        ┗ __init__,py
        ┗ interface.py
        ┗ style.py

      ┗ performer
        ┗ __init__.py
        ┗ handler.py
        ┗ performer.py
        ┗ unsunghero.py

      ┗ system
        ┗ fonts
          ┗ ...
        ┗ images
          ┗ ...
        ┗ log
          ┗ ...
        ┗ report
          ┗ ...

      ┗ mogicasher.py

または※

    dist
    ┗ casher
      ┗ system
        ┗ fonts
          ┗ ...
        ┗ images
          ┗ ...
        ┗ log
          ┗ ...
        ┗ report
          ┗ ...

      ┗ mogicasher.exe

※casher.pyをexe化した場合の構成

## 使い方
### 基本操作
基本的には[コード読み取り](/README.md#コードを読み取る)と[精算](/README.md#清算する)の繰り返しです。  
コンビニと同じように、**一人来る→バーコード通す→お会計**のノリっていえば分かりやすいかな？

#### 下準備
[CSVファイルの形式](/README.md#CSVファイルの形式)に記述した形式のCSVファイルを用意しよう。

#### 起動
casher.pyを実行するとGUIが立ち上がります。(exe化した場合はexeファイルをクリック)  
起動時の画面はこんな感じ。

![home](https://user-images.githubusercontent.com/88261399/128629556-b5db2d87-7417-4985-9491-0903cca7b8aa.png)

#### 模擬店モード
このソフト一つでチケット売り場と模擬店の両方に対応するために、模擬店モードが実装されています。  
模擬店で使用する場合は"Collect"のチェックボックスにチェックを入れてください。  
["Check Out"](/README.md#精算する)機能が無効になって、ひたすら読んだバーコードを表に追加していきます。

#### コードデータを読み込む
##### 初回起動時

Load ModeでCSVを読み込む  
"Load Mode"にチェックを入れるとLoad画面に切り替わります。  
"Browse"ボタンをクリックするとファイル選択画面が表示されるので、用意したCSVファイルを選択して読み込んでください。

![loadmode](https://user-images.githubusercontent.com/88261399/128630723-30b0cf32-d071-4e1d-8b42-2022dc6e51a4.png)

##### 続きから始める
このソフトには、終了時に自動でデータを保存する機能がついています。  
前回の続きから始める場合、起動したときに最新のデータが自動で読み込まれるので操作は必要ありません。  
***
読み込んだらLoad Modeが自動で解除されて、右側の表が更新されます。  

![loaded](https://user-images.githubusercontent.com/88261399/128630715-6511ddd3-b2be-4919-b81e-5544dac7a97a.png)

#### コードを読み取る
バーコードリーダーを使ってコードを読み取ると、このような画面になります。  
**データにないコードはスルーされます。** Enter空打ちや数字以外も同じです。  
⚠️ *実際のレジでいえば精算前の状態です。まだ売り上げとして確定していません。*

![input](https://user-images.githubusercontent.com/88261399/128632132-aad711ff-e80d-4369-99fc-bf38f5b4cc2e.png)

#### 精算する
バーコードをひと通り通し終わったら、"Check Out"ボタンをクリックしてください。  
ボタンを押すまでに読み取ったコードが全て処理されます。
**この時点で初めて売り上げにカウントされます。**

![checkout](https://user-images.githubusercontent.com/88261399/128632357-39664c29-4c73-4c20-b9d9-e1d68d0789e7.gif)
***
"Cancel"ボタンをクリックすると、未確定の売り上げがリセットされます。  
読み取りを間違えたときに使ってね。

![cancel](https://user-images.githubusercontent.com/88261399/128704622-f4b6fb7e-e069-4624-bf37-7643be90d84e.gif)

#### ソフトを終了する
"Exit"ボタンあるいは電源のアイコンをクリックしてください。  
終了時にその時点での売り上げデータが勝手にCSVで保存されます。

![exit](https://user-images.githubusercontent.com/88261399/128704680-5c37e31e-7354-4f62-8b0a-7fd453c1dba8.gif)

### Analyze

### Setting
設定画面が作れるような複雑なソフトじゃないけど無理やり作った。
変更の反映にはRestartボタンで再起動が必要です。
- Darkmode
  - 今流行りのダークモードを実装してみた。
  - チェックを入れて再起動するとダークモードになる。
  - ダークモードの状態でチェックを外して再起動するとライトモードに戻る。
- Custom Color
  - GUIのテーマを好きなように選べるようにしてみた。
  - チェックを入れて、どれか選んだ状態で再起動するとテーマが反映される。
  - チェックを外すと選んだテーマは反映されない。
  - ちなみにダークモードをオンにして再起動すると、テーマを選んでいてもダークモードになる。
- Custom Font
  - SanFranciscoっていう普通PCに入ってないフォントで作ったので、インストールできるようにした。
  - subprocessでフォントを開いてユーザーにインストールさせる。システムフォルダにコピーするコードなんか書くとウイルス判定食らうからね
  - なおファイルの配布はややこしそうなのでここでは[fonts](/fonts/fonts.md)にてフォント名を書くのみにした。
- Delete Logs
  - 自動保存データ(*log*内のデータ)を全削除できるようにした。
  - マジで一発で全部消えるから気を付けてね...
- Sourcecode
  - [このGitHubリンク](/)を開く。
  - せっかくなのでソフトを配ったみんなに見てもらえるようにした。

## 注意事項
- 複数データの同時使用  
このソフトは、同時に一つのバーコードデータが使われることを想定しています。  
コードや値段が異なるCSVファイルを混ぜて使うとlogフォルダが荒れるので、自動読み込み機能が正しく機能しなくなります。  
別のデータに切り替えたい場合は、Setting画面の"Clear Logs"ボタンをクリックしてlogフォルダ内をリセットしてください。
## 解説
プログラム的に説明します。
### リスト
このソフトは以下のリストを使います。  
全ての処理はこのリストに基づきます。  
ちなみにこれらに合計金額は含まれず、関数を使って合計金額を計算し**表示する**仕組みです。
```
# 読み込んだCSVデータを変換したリスト
# 確定した売り上げの計算に使う。
database = [["#1", "xxxxxxxx", xxx, xxx], ...]

# 読み取ったバーコードを追加していくリスト
# Check Out前の仮の売り上げの計算に使う。
history = ["xxxxxxxx", "xxxxxxxx", ...]
```
### バーコード読み取り時
ざっくり画像で解説するとこんな感じ。  
![reading](https://user-images.githubusercontent.com/88261399/128671421-aef9b048-8b70-48c8-8e36-6fa042a07b55.png)

具体例で説明してみましょう。  
画面のこの部分が変わります。  
![subtotal](https://user-images.githubusercontent.com/88261399/128665494-fa5a3d79-2bb4-4010-9957-828dd2c0313b.png)  
以下のコードで登録されたバーコード以外をブロックします。
```
input = 入力値
window = PySimpleGUIのオブジェクト

# databaseの"CODE"列からコードの一覧を作る
codes = [database[x][1] for x in range(len(database))]

try:
   # "codes.index(input)"で、inputがcodesに含まれない場合エラーが出る。
   # 入力欄のすぐ下にある、入力値のタグや値段を表示するテキストをupdateする。
   # 正常に処理が行われた場合、historyにinputが追加される。
   
   tag = database[codes.index(input)][0]
   price = database[codes.index(input)][2]
   
   history.append(input)
   
   window["-RECENT-"].update(">{} {} ¥{}".format(tag, input, price))
   
except ValueError:
   # エラーが出た場合inputを無視する。
   pass
```
また、精算機能に対応するため支払金額を表示する必要があります。  
なおこのプログラムは入力があるたびに、↑のtry節の続きに実行されます。
```
...
history.append(input)

def calc_subtotal(database, history):
   # databaseを使って品目ごとにhistory内のコードの数を数え、それぞれ値段を掛ける。
   # つまり品目ごとの売り上げが出るので、それをsubtotalに足していく。
   
   # 一時データの売り上げを格納する変数
   subtotal = 0
   
   for x in database:
      subtotal += history.count(x[1])*x[2]
   
   # 仮の売り上げを返す
   return subtotal

# "Subtotal"テキストを更新する
window["-SUBTOTAL-"].update("¥{}".format(calc_subtotal(database, history)))
```