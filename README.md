# mypkg

ロボットシステム学講義用のリポジトリ

[![test](https://github.com/ishida777/mypkg/actions/workflows/test.yml/badge.svg)]

### talker
0.5秒ごとに数字を足し、メッセージで結果を表示する

### listener
talkerから送られてきたメッセージを出力する

### 使用方法
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
