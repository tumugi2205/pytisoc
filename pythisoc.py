import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import random
from wall import wall
from people import people
from chase import chase
# %matplotlib inline 表示だとアニメーションしない

def main_function(wideth):
    fig = plt.figure(dpi=100, figsize=(wideth,wideth))
    ax = fig.add_subplot()
    # plt.grid(color='gray')
    # plt.grid(which='minor')
    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])

    # plt.gca().xaxis.set_minor_locator(tick.MultipleLocator(1))
    # plt.gca().yaxis.set_minor_locator(tick.MultipleLocator(1))

    max_x = 51
    max_y = 51
    map_data, wall_list, oblist = init_map(max_x, max_y)
    for o in wall_list:
        plot(o)

    # 周波数を高くしていく
    while True:
        line = []
        update_map(oblist, map_data, line)
        plt.pause(1/60)
        [i.remove() for i in line]
        # step_end(map_data)


def init_map(max_x, max_y):
    """シミュレーション開始時に実行される関数
    Returns:
        tuple: xのデータ, yのデータ
    """
    map_data = [[ {} for x in range(max_x) ] for y in range(max_y) ]
    wall_list = []
    for x in range(51):
        map_data[x][0]["wall"] = wall(x,0,"red")
        map_data[0][x]["wall"] = wall(0,x,"red")
        map_data[x][50]["wall"] = wall(x,50,"red")
        map_data[50][x]["wall"] = wall(50,x,"red")
        wall_list.append(map_data[x][0]["wall"])
        wall_list.append(map_data[0][x]["wall"])
        wall_list.append(map_data[x][50]["wall"])
        wall_list.append(map_data[50][x]["wall"])
    
    oblist = []
    for i in range(100):
        while True:
            rx = random.randint(1, 49)
            ry = random.randint(1, 49)
            if not map_data[rx][ry]:
                map_data[rx][ry]["people"] = people(rx,ry,"blue")
                oblist.append(map_data[rx][ry]["people"])
                break
        
    for i in range(10):
        while True:
            rx = random.randint(1, 49)
            ry = random.randint(1, 49)
            if not map_data[rx][ry]:
                map_data[rx][ry]["chase"] = chase(rx,ry,"blue")
                oblist.append(map_data[rx][ry]["chase"])
                break
    return map_data, wall_list, oblist


def update_map(oblist, map_data, line):
    """ステップごとに実行される関数

    Returns:
        tuple: xのデータ, yのデータ
    """
    for o in oblist:
        line.append(plot(o))
    for o in oblist:
        o.update(map_data)

def step_end(oblist):
    for o in oblist:
        o.end(oblist)

def plot(data):
    """座標データをxとyに変換する

    Args:
        data (dict): 辞書型のマップデータ

    Returns:
        tuple: xのデータ, yのデータ
    """
    marker = data.marker
    c = data.color
    x = data.x+0.5
    y = data.y+0.5
    return plt.scatter(x, y, s=100, marker=marker, c=c)


main_function(10)