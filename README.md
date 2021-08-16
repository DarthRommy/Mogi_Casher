# MogiCasher
![Current version](https://img.shields.io/badge/MogiCasher-1.5.1-red)
![Python version](https://img.shields.io/badge/Python-3.9.6-blue)
![PySimpleGUI version](https://img.shields.io/badge/PySimpleGUI-4.45.0-orange)
![pandas version](https://img.shields.io/badge/pandas-1.3.1-green)

Readmeにようこそ！
使い方の画像の更新は本体のアプデよりかなり遅いことをご了承ください。

**いろんなことが適当に書いてあります！！！**

## 目次
1. [使い方](/README.md#使い方)
   - [基本操作](/README.md#基本操作)
   - [Analyze](/README.md#Analyze)
   - [Setting](/README.md#Setting)
1. [概要](/README.md#概要)
   - [動作環境](/README.md#動作環境)
   - [CSVファイルの形式](/README.md#CSVファイルの形式)
   - [対応コード](/README.md#対応コード)
   - [ファイル構成](/README.md#ファイル構成)
1. [解説](/README.md#解説)
   - [リスト](/README.md#リスト)
   - [バーコード読み取り時](README.md#バーコード読み取り時)
1. [補足](/README.md#補足)

## 使い方
### 基本操作
基本的には[コード読み取り](/README.md#コードを読み取る)と[精算](/README.md#清算する)の繰り返しです。  
コンビニと同じように、**一人来る→バーコード通す→お会計**のノリっていえば分かりやすいかな？

#### 下準備
[CSVファイルの形式](/README.md#CSVファイルの形式)に沿ったCSVファイルを用意しよう。ExcelかSpreadsheetで作るのがいいね

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

## 概要
CSVファイルとリストを使用する(コアの部分は)シンプルなソフトです。  
システムの参考 -> [LC_Manager](https://github.com/parsely1231/LC_Manager)
- [x] リストがかさばらないので動作が早い！
- [x] 会計機能がついてる！
- [x] ぱっと見で売り上げが分かる！
- [x] 終了するときにオートセーブしてくれる！
- [x] 次の起動時にオートセーブしたデータを読み込んでくれる！
- [ ] 日本語でいい感じのフォントがなかったから仕方なく英語UI&英語フォントに...
- [ ] オフラインソフトだから模擬店間のリアルタイムなデータ同期はできない...
- [ ] バーコード画像の生成機能はない...

### 動作環境
Python3のソフトです。動作には以下の外部ライブラリが必要です。*[アプリケーション化]*(/README.md#補足)  
- [pandas](https://pandas.pydata.org/)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)

### CSVファイルの形式
- UI的には5品目を想定していますが、**何品目でも対応できます。**
- ~~名前は *profile.csv* にしてください。ただし前後には何を入れてもOKです。 ex.) profile_0806.csv~~
- ~~CSVのカラムは、コードの列を除き指定はありません。コードの列のみ"***CODE***"にしてください。~~
- 最初に読み込むCSVのファイル名はなんでもええで
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
mogicasherフォルダの名前は変えてもOKです。

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
    ┗ mogicasher
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

## 解説
基本のシステムだけ説明しときます。

### リスト
このソフトは以下のリストを使います。  
全ての処理はこのリストに基づきます。  
ちなみにこれらに合計金額は含まれず、関数を使っていちいち合計金額を計算し表示する仕組みです。
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
input: 入力値
window: PySimpleGUIのWindowオブジェクト

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
以下のプログラムは入力があるたびに、↑のtry節の続きに実行されます。
```
...
history.append(input)

def calc_subtotal(database, history):
   # databaseを使ってコードごとのhistory内の数を数え、それぞれ値段を掛ける。
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

## 補足
Pythonかじってる人向け

### レイアウト変更
MogiCasherはPySimpleGUIを使用してます。  
レイアウトの記述方法は[PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/call%20reference/)に従ってください。  
また、引数が多くて見にくくなるものは[style.py](/mogicasher/interface/casher.py)のように別で辞書型宣言することもできます。

### アプリケーション化
[mogicasher.py](/mogicasher/mogicasher.py)を指定してください。  
作者は設定ファイルを書くのがめんどくさいので[pysintaller](https://www.pyinstaller.org/)を使ってます。  
※起動は結構重たいです。pyinstallerのせいかPySimpleGUIのせいかは知らんけど

### 複数データの同時使用  
オートセーブしたデータを読み込む関数がこちら。 (一部改変)
```
def get_autosave():

  # logフォルダ内のファイル一覧をゲットして作成日時で並べ替える
  path = f"{(os.getcwd()}/log/*.csv"
  files = glob.glob(path)
  files.sort(reverse=True, key=lambda x: os.path.getctime(x))

  # 完全にtry節にハマってしまった
  try:
      df = pd.read_csv(files[0], dtype={0: str, 1: str, 2: int, 3: int}, on_bad_lines="error")
      def_database = df.values.tolist()

      # 1行でも要素が4以外ならエラー判定
      for x in def_database:
          if len(x) > 4 or len(x) < 4:
              raise ValueError()
  
  # エラーが出た場合デフォルトのリストになる
  except (IndexError, ValueError):
      def_database = [[f"#{x+1}", "xxxxxxxx", 0, 0] for x in range(5)]

  return def_database
```
*os.path.getctime()* はファイルの作成日時を取得する関数。  