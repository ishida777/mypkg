# mypkg

![test](https://github.com/ishida777/mypkg/actions/workflows/test.yml/badge.svg)

このリポジトリは2023年度ロボットシステム学講義で作成、使用したリポジトリです。

talkerとlistenerの二つのノード間で通信を行うROS2のパッケージです。

## talkerとlistenerについて
### talker
実行すると0.5秒ごとに数字を0から一つずつ足し、Int16型のメッセージをcountupというトピックを通じてパブリッシュする

* 使用方法
```
$ ros2 run mypkg talker
```
### listener
talkerから送られてきたメッセージを出力する

talkerと同時に実行する場合はtalkerとは別の端末から操作する必要がある
* 使用方法
```
$ ros2 run mypkg listener
[INFO] [1704306103.850181182] [listener]: Listener:0
[INFO] [1704306104.343492538] [listener]: Listener:1
[INFO] [1704306104.842904671] [listener]: Listener:2
[INFO] [1704306105.344368203] [listener]: Listener:3
[INFO] [1704306105.843012234] [listener]: Listener:4
[INFO] [1704306106.343370339] [listener]: Listener:5
[INFO] [1704306106.842876002] [listener]: Listener:6
[INFO] [1704306107.342970278] [listener]: Listener:7
[INFO] [1704306107.843290063] [listener]: Listener:8
[INFO] [1704306108.342993509] [listener]: Listener:9
[INFO] [1704306108.844218066] [listener]: Listener:10
```

### トピック
通信の型に、16ビットの符号付き整数を使用

## talk_listen.launch.pyについて
talkerとlistenerの二つを同時に実行できる
### 使用方法
```
ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/shiba777/.ros/log/2024-01-04-01-55-29-065219-LAPTOP-R2BVUG5M-9959
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [9961]
[INFO] [listener-2]: process started with pid [9963]
[listener-2] [INFO] [1704300929.963305720] [listener]: Listener:0
[listener-2] [INFO] [1704300930.438671231] [listener]: Listener:1
[listener-2] [INFO] [1704300930.939169119] [listener]: Listener:2
[listener-2] [INFO] [1704300931.439552390] [listener]: Listener:3
[listener-2] [INFO] [1704300931.939170777] [listener]: Listener:4
[listener-2] [INFO] [1704300932.439530528] [listener]: Listener:5
[listener-2] [INFO] [1704300932.939123163] [listener]: Listener:6
[listener-2] [INFO] [1704300933.439155826] [listener]: Listener:7
[listener-2] [INFO] [1704300933.938676775] [listener]: Listener:8
[listener-2] [INFO] [1704300934.438806666] [listener]: Listener:9
[listener-2] [INFO] [1704300934.938913867] [listener]: Listener:10
```

## 動作環境
### 必要なソフトウェア
* Python
    * テスト済み: 3.7 ~ 3.10

## テスト環境
* ubuntu22.04

### 著作権
* このソフトウェアパッケージは、三条項BSDライセンスの下、再頒布および使用が許可されます。
    * このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slide/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
    * © 2023 KotaYoshiba
