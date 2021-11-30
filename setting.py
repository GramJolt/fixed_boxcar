import Box2D
from Box2D.b2 import *
from Box2D import *

import os
import datetime

curdir = os.getcwd()
print("現在のディレクトリ", curdir)

now = datetime.datetime.now()
filename = 'GA_boxcar2d_' + now.strftime('%Y%m%d_%H%M%S')
filename1 = 'log_' + now.strftime('%Y%m%d_%H%M%S' + '.csv')
filename2 = 'log_' + now.strftime('%Y%m%d_%H%M%S' + '_all.csv')
filename3 = 'img_' + now.strftime('%Y%m%d_%H%M%S' + '.png')
print("ログフォルダ名", filename)
print("各世代の最良値が入ったファイル", filename1)
print("各世代の全個体の評価値が入ったファイル", filename2)

seed_value = now.strftime('%Y%m%d_%H%M%S')

groundPieceWidth = 1.5
groundPieceHeight = 0.15

chassisMaxAxis = 1.1
chassisMinAxis = 0.1
chassisMinDensity = 50
chassisMaxDensity = 100

wheelMaxRadius = 0.5
wheelMinRadius = 0.2
wheelMaxDensity = 30
wheelMinDensity = 10
motorSpeed = 25
gravity = b2Vec2(0.0, -9.81)
doSleep = True
start_position = b2Vec2(1,2)

max_health = 100

MAX_NUM_WHEEL_VERTEX = 8


# 車輪の最大数
MAX_NUM_WHEEL = 2

# 遺伝子の長さ
LEN_GENOME = 20

# 個体数
population_size = 20

#世代更新回数
MAX_GEN = 125

#グラフのソート方法 0はなし、1は全個体まとめてソート、2は世代ごとにソート
SORT_VALUE = 0

#True or Falseで、グラフを画面出力のオンオフ。Trueだと最適化が世代ごとで一時停止するので、グラフを手動で×する
SHOW_GRAPH = False

#タイヤの数が0の個体をつくるかどうか True or False 
NO_WHEEL = True