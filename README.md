# MogiCasher
![Current version](https://img.shields.io/badge/MogiCasher-1.5.3-red)
![Python version](https://img.shields.io/badge/Python-3.9.6-blue)
![PySimpleGUI version](https://img.shields.io/badge/PySimpleGUI-4.45.0-orange)
![pandas version](https://img.shields.io/badge/pandas-1.3.1-green)

引継ぎでガチャガチャしそうやしGitHubに上げとくで。  

# 目次
1. [使い方](/README.md#使い方)
   - ざっくり使い方を説明してみた。説明書代わりに使ってね（更新停止中）
1. [詳しく](/README.md#詳しく)
   - 2021年の模擬の集計システムも含めてこのソフトを解説してみた。

# 使い方
※更新停止中

## 基本操作
基本的には[コード読み取り](/README.md#コードを読み取る)と[精算](/README.md#清算する)の繰り返しです。  
コンビニと同じように、**一人来る→バーコード通す→お会計**のノリっていえば分かりやすいかな？

### 下準備
[CSVファイルの形式](/README.md#CSVファイルの形式)に沿ったCSVファイルを用意しよう。ExcelかSpreadsheetで作るのがいいね
※実際配って使うときはフォルダ内に一緒に入れてある

### 起動
mogicasher.exe(mogicasher.py)を実行するとGUIが立ち上がります。  
多分警告とかなくすんなり起動できると思う。  
起動時の画面はこんな感じ。


### コードデータを読み込む
#### 初回起動時
"Browse"ボタンをクリックするとファイル選択画面が表示されるので、用意したCSVファイルを選択して読み込んでください。

#### 続きから始める
このソフトには、終了時にデータをオートセーブする機能がついています。  
前回の続きから始める場合、最新のデータが読み込まれた状態で起動するので操作は必要ありません。  
***
正常に読み込んだら右側の表が更新されます。  
変なデータだったら変わりません。

### コードを読み取る
バーコードリーダーを使ってコードを読み取ると、このような画面になります。  
**データにないコードはスルーされます。** Enter空打ちも同じです。  

### 精算する
バーコードをひと通り通し終わったら、"Check Out"ボタンをクリックしてください。  
ボタンを押すまでに読み取ったコードが全て処理されます。
**この時点で初めて売り上げにカウントされます。**

***
"Cancel"ボタンをクリックすると、未確定の売り上げがリセットされます。  
読み取りを間違えたときに使ってね。


### ソフトを終了する
"Exit"ボタン、電源のアイコン、右上の×ボタンのどれかをクリックしてください。  
終了時にその時点での売り上げデータがオートセーブされます。

## Setting
設定画面が作れるような複雑なソフトじゃないけど無理やり作った。  
DarkmodeとCustom Fontの反映にはRestartボタンで再起動が必要です。
- 入力欄
  - 保存データの識別用に発団名を設定できるようにしてみた。
  - Submitボタンを押すと入力欄に打ち込んだ文字が登録される。
  - 再起動すると左上のタイトルが発団名になるぜ
- Darkmode
  - 今流行りのダークモードを実装してみた。
  - チェックを入れて再起動するとダークモードになる。
  - ダークモードの状態でチェックを外して再起動するとライトモードに戻る。
- Custom Font
  - SanFranciscoっていう普通PCに入ってないフォントで作ったので、インストールできるようにした。
  - subprocessでフォントを開いてユーザーにインストールさせる。システムフォルダにコピーするコードなんか書くとウイルス判定食らうからね
  - なおファイルの配布はややこしそうなのでここでは[fonts](/mogicasher/system/system.md)にてフォント名を書くのみにした。
- Delete Log
  - 自動保存データ(*log*内のデータ)を全削除できるようにした。
  - マジで一発で全部消えるから気を付けてね...
- Delete Report
  - Analyze用データ(*report*内のデータ)を全削除できるようにした。
  - 押した後はRefreshしよう（まあ一応エラーは吐かないようにしてあるけど）
- Sourcecode
  - [このGitHubリンク](/)を開く。
  - せっかくなのでソフトを配ったみんなに見てもらえるようにした。

# 詳しく
CSVファイルとリストを使用するだけのシンプルなソフト。  
システムの参考 -> [LC_Manager](https://github.com/parsely1231/LC_Manager)

## 機能一覧
- [x] バーコードリーダーを使ったバーコード読み取り
- [x] 未登録コードのブロック
- [x] 一旦保留して後でまとめて売り上げに加算できる小計機能（なくなるかも）
- [x] 売上個数と金額が一目でわかる表
- [x] 終了時にCSV形式でデータを自動保存
- [x] 最新の自動保存データを読み込んだ状態で起動
- [x] 保存ファイル識別用の発団名登録機能
- [x] ダークモード搭載
- [ ] 模擬店間のリアルタイムなデータ同期は不可

## 動作環境
Python3のソフトです。動作には以下の外部ライブラリが必要です。  
- [pandas](https://pandas.pydata.org/)
- [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)

## CSVファイルの形式
- 何品目でも対応可。
- Loadで読み込むCSVのファイル名はなんでもOK。
- カラム名（CODEとかPRICEとか）はどの列も指定なし。
- タグ列もどんな文字列でもOK。
  - ※英語フォントなのでアルファベット以外は表示がダサい

| (tag) | CODE | PRICE | UNITS |
| ---: | ---: | ---: | ---: |
| #1 | xxxxxxxx | xxx | xxx |
| #2 | xxxxxxxx | xxx | xxx |
| ... | ... | ... | ... |

## 対応コード

バーコードリーダーが読み取れるならなんでもOK。  
例) EAN(JAN)13桁/8桁, CODE39, CODE128, etc...

## ファイル構成
このソフトのファイル構成です。  
mogicasherフォルダの場所や名前は変えてもOK。**中身はダメ**  
```
dist
┗ mogicasher
  ┗ interface
    ┗ __init__.py
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
```
または※
```
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
```
※casher.pyをexe化した場合の構成

### 各ファイルの説明
- [interface.py](/mogicasher/interface/interface.py)  
ウィンドウのレイアウトを書いた場所。

- [style.py](/mogicasher/interface/style.py)  
ウィンドウのレイアウトのうち、引数が多くなるものについて辞書型でまとめた。

- [handler.py](/mogicasher/performer/handler.py)  
ウィンドウ上のイベントを受け取り、それに応じて関数を実行する。

- [performer.py](/mogicasher/performer/performer.py)  
イベントに応じてhandlerに呼び出される関数を書いた場所。

- [unsunghero.py](/mogicasher/performer/unsunghero.py)  
ウィンドウに直接影響しない(=Interfaceのインスタンスを使わない)関数をまとめた場所。

- [mogicasher.py](/mogicasher/mogicasher.py)  
ウィンドウの起動から終了までの全ての処理をまとめる場所。

## バーコードどうやって入れてんの？
1. バーコードリーダーは読み取ったときにEnterを送信する
1. バーコードリーダーの出力はキーボード入力と同じ  
-> 読み取った値はInput欄に入力される
1. PySimpleGUIのWindowオブジェクトには"return_keyboard_events"という引数がある  
-> Trueにするとキーボード入力をイベントとして処理してくれる

つまり、Enter="/r"イベントが発生したときにInput欄の値を判定するようにしたってわけ

## シンプルなソフトとは
シンプルとか言うといてなに6つもファイル分かれてんねん！と思ったやろ？  
一応今後いじりやすいように関数の機能ごとに分けてみたんですが、にしてもいらん機能つけすぎたな
- レイアウトを切り替えられるようにしてみたり  
Pythonでモダンなソフトを作るとか狂気の沙汰やろ -> [change_layout](/mogicasher/performer/performer.py#L20)
- 流行りのダークモードを実装してみたり  
ダークモードの反映のための再起動の機能を付けたせいで[余計な関数](/mogicasher/mogicasher.py#L15)が増えてしまった

### 方針
それはともかく、細かいウィンドウの話を取っ払ったあとのシステムはめちゃくちゃシンプル。  
**そんなにかさばらないリストをひたすらfor~in文でぶん回すシステムです。**  
読み取ったコードを全部突っ込んだクッソ重いリストがあるわけではありません。  

使うのはこのリストだけ。
```
#CSVのデータをvalues.tolist()で二重リストにしただけ
database = [["#1", "xxxxxxxx", xxx, xxx],...]

# 読んだコードを一時保存しておくリスト
history = ["xxxxxxxxx",...]
```
どちらのリストにも売り上げの枠はありません。  
このリストを使って都度計算してウィンドウに表示するだけ、という感じ。

### バーコードの判定
Input欄の入力値を判定する関数はこんな感じ。  
知らないコードのブロック装置も含んでます。 -> [handle_input](/mogicasher/performer/performer.py#L51)
```
def handle_input(values, database):
   code = values["-INPUT-"]
   
   codes = [x[1] for x in database]
   
   try:
      tag = database[codes.index(code)][0]
      price = database[codes.index(code)][2]
      
      history.append(code)
      
   except ValueError:
      pass
```
`values["-INPUT-"]`...Input欄の値  
`[x[1] for x in database]`...`database`からコードの一覧を取得  
`tag`, `price`...ウィンドウにタグと値段を表示するための変数

変数tagの `codes.index(code)` の部分で、`code`が`codes`に含まれない場合は例外処理でスルーする。(ValueError)  
まあつまりブロック装置はウィンドウありきってことですね

### 売り上げ登録
Chekcoutボタンを押すと、初めて`database`に売上個数が追加されます。 -> [checkout](/mogicasher/performer/performer.py#L124)
```
def checkout(database, history):
   for x in database:
      x[3] += history.count(x[1])
   history.clear()
```
各コードごとに`history`内に何個あるか数えて、その個数をもとの個数に足す。  
終わったら`history`はリセットしてしまいましょう。

### 売り上げ計算
売り上げ計算も簡単。
```
def update_totaly(database):
   total = 0
   for x in database:
      total += x[2]*x[3]
   return total
```
各コードごとに値段と個数を掛けて、`total`に足していく。  
終わったら`total`をreturnするだけ。  
ウィンドウに表示するために使うだけですが、意外と何回か使うので関数にしました。
