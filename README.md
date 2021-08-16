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


#### コードデータを読み込む
##### 初回起動時

Load ModeでCSVを読み込む  
"Load Mode"にチェックを入れるとLoad画面に切り替わります。  
"Browse"ボタンをクリックするとファイル選択画面が表示されるので、用意したCSVファイルを選択して読み込んでください。


##### 続きから始める
このソフトには、終了時に自動でデータを保存する機能がついています。  
前回の続きから始める場合、起動したときに最新のデータが自動で読み込まれるので操作は必要ありません。  
***
読み込んだらLoad Modeが自動で解除されて、右側の表が更新されます。  


#### コードを読み取る
バーコードリーダーを使ってコードを読み取ると、このような画面になります。  
**データにないコードはスルーされます。** Enter空打ちや数字以外も同じです。  
⚠️ *実際のレジでいえば精算前の状態です。まだ売り上げとして確定していません。*


#### 精算する
バーコードをひと通り通し終わったら、"Check Out"ボタンをクリックしてください。  
ボタンを押すまでに読み取ったコードが全て処理されます。
**この時点で初めて売り上げにカウントされます。**

***
"Cancel"ボタンをクリックすると、未確定の売り上げがリセットされます。  
読み取りを間違えたときに使ってね。


#### ソフトを終了する
"Exit"ボタンあるいは電源のアイコンをクリックしてください。  
終了時にその時点での売り上げデータが勝手にCSVで保存されます。

### Analyze
各模擬店の売り上げを見られるようにした。  
ちなみにオフラインなので終わった後にCSVを物理でコピーしないといけません

#### データを追加する
Browseボタンをクリックするとファイル選択画面が出てきます。  
欲しいデータを選んでからRefreshすると、表に反映されます。

#### データを見る
プルダウンメニューから見たいデータを選んでね
##### Overall
reportフォルダ内にあるファイルそれぞれの名前と合計金額を表示します。

##### それ以外
各ファイルのタグとタグごとの売り上げ、そして全体の売り上げを表示します。

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
- Delete Log
  - 自動保存データ(*log*内のデータ)を全削除できるようにした。
  - マジで一発で全部消えるから気を付けてね...
- Delete Report
  - Analyze用データ(*report*内のデータ)を全削除できるようにした。
  - 押した後はRefreshしよう（まあ一応エラーは吐かないようにしてあるけど）
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
Python3のソフトです。動作には以下の外部ライブラリが必要です。-> *[アプリケーション化](/README.md#補足)*  
- [pandas](https://pandas.pydata.org/)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)

### CSVファイルの形式
- UI的には5品目を想定していますが、**何品目でも対応できます。**
- 最初に読み込むCSVのファイル名はなんでもええで
- CSVのカラム名はどの列も指定はありません。
- また、下では1列目が#~の連番ですが、**どんな文字列にしても問題ありません。**
  - ※英語フォントなのでアルファベット以外は表示がダサくなります。

| (tag) | CODE | PRICE | UNITS |
| ---: | ---: | ---: | ---: |
| #1 | xxxxxxxx | xxx | 0 |
| #2 | xxxxxxxx | xxx | 0 |
| ... | ... | ... | ... |
| #5 | xxxxxxxx | xxx | 0 |

### 対応コード

バーコードリーダーが読み取れるならなんでもあり

### ファイル構成
このソフトのファイル構成です。
mogicasherフォルダの名前は変えてもOK。

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
また、引数が多くて見にくくなるものは[style.py](/mogicasher/interface/style.py)のように別で辞書型宣言することもできます。

### アプリケーション化
[mogicasher.py](/mogicasher/mogicasher.py)を指定してください。  
作者は設定ファイルを書くのがめんどくさいので[pysintaller](https://www.pyinstaller.org/)を使ってます。  
※起動は若干重たいです。pyinstallerのせいかPySimpleGUIのせいかは知らんけど
