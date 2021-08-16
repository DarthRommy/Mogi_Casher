# MogiCasher
![Current version](https://img.shields.io/badge/MogiCasher-1.5.2-red)
![Python version](https://img.shields.io/badge/Python-3.9.6-blue)
![PySimpleGUI version](https://img.shields.io/badge/PySimpleGUI-4.45.0-orange)
![pandas version](https://img.shields.io/badge/pandas-1.3.1-green)

Readmeにようこそ！  
引継ぎでガチャガチャしそうなのでGitHubに上げてしまいました。  
来年の担当者は好きにコードいじっちゃってください。

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
DarkmodeとCustom Fontの反映にはRestartボタンで再起動が必要です。
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
- 何品目でも対応できます。
- Loadで読み込むCSVのファイル名はなんでもOK。
- CSVのカラム名はどの列も指定なし。
- また、下では1列目が#~の連番ですが、**どんな文字列にしてもOK。**
  - ※英語フォントなのでアルファベット以外は表示がダサくなります。

| (tag) | CODE | PRICE | UNITS |
| ---: | ---: | ---: | ---: |
| #1 | xxxxxxxx | xxx | 0 |
| #2 | xxxxxxxx | xxx | 0 |
| ... | ... | ... | ... |
| #5 | xxxxxxxx | xxx | 0 |

### 対応コード

バーコードリーダーが読み取れるならなんでもOK。  
例) EAN(JAN)13桁/8桁, CODE39, CODE128, etc...

### ファイル構成
このソフトのファイル構成です。
mogicasherフォルダの名前は変えてもOK。  
各スクリプトファイルについては[補足](/README.md#補足)

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

## 補足
Pythonかじってる人向け

### 各ファイルの説明
- interface.py  
ウィンドウのレイアウトを書いた場所。  
class: Interface  
Location: [interface.py](/mogicasher/interface/interface.py)

- style.py  
ウィンドウのレイアウトのうち、引数が多くなるものについて辞書型でまとめた。  
class: None  
Location: [style.py](/mogicasher/interface/style.py)

- handler.py  
ウィンドウ上のイベントを受け取り、それに応じて関数を実行する。  
class: Handler  
Location: [handler.py](/mogicasher/performer/handler.py)

- performer.py  
イベントに応じてhandlerに呼び出される関数を書いた場所。  
class: Performer  
Location: [performer.py](/mogicasher/performer/performer.py)

- unsunghero.py  
ウィンドウに直接影響しない(=Interfaceのインスタンスを使わない)関数をまとめた場所。  
class: UnsungHero  
Location: [unsunghero.py](/mogicasher/performer/unsunghero.py)

- mogicasher.py  
ウィンドウの起動から終了までの全ての処理をまとめる場所。  
class: MogiCasher  
Location: [mogicasher.py](/mogicasher/mogicasher.py)

### レイアウト変更
MogiCasherはPySimpleGUIを使用してます。  
レイアウトの記述方法は[PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/call%20reference/)に従ってください。  
また、引数が多くて見にくくなるものは[style.py](/mogicasher/interface/style.py)のように別で辞書型宣言することもできます。

### アプリケーション化
[mogicasher.py](/mogicasher/mogicasher.py)を指定してください。  
作者は設定ファイルを書くのがめんどくさいので[pysintaller](https://www.pyinstaller.org/)を使ってます。  
※起動は若干重たいです。pyinstallerのせいかPySimpleGUIのせいかは知らんけど
