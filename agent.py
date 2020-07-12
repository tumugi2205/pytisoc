import random
import json
from tmpObj import tmpObj
import map_look_list

# check_list = []
# with open("look.json") as f:
#     check_list = json.load(f)

def move_front(obj, map_data, point):
    if obj.obj_dir == 0:
        map_data[obj.x+point][obj.y][obj.type] = map_data[obj.x][obj.y].pop(obj.type)
        obj.x = obj.x + point
    elif obj.obj_dir == 1:
        map_data[obj.x][obj.y-point][obj.type] = map_data[obj.x][obj.y].pop(obj.type)
        obj.y = obj.y - point
    elif obj.obj_dir == 2:
        map_data[obj.x-point][obj.y][obj.type] = map_data[obj.x][obj.y].pop(obj.type)
        obj.x = obj.x - point
    else:
        map_data[obj.x][obj.y+point][obj.type] = map_data[obj.x][obj.y].pop(obj.type)
        obj.y = obj.y + point

def turn(obj, turn):
    obj.obj_dir = (4 + obj.obj_dir + turn) % 4
    marker_list = [">", "v", "<", "^"]
    obj.marker = marker_list[obj.obj_dir]

def check_front(obj, map_data, obj_list):
    if obj.obj_dir == 0:
        if [x for x in map_data[obj.x+1][obj.y] if x in obj_list]:
            return True
    elif obj.obj_dir == 1:
        if [x for x in map_data[obj.x][obj.y-1] if x in obj_list]:
            return True
    elif obj.obj_dir == 2:
        if [x for x in map_data[obj.x-1][obj.y] if x in obj_list]:
            return True
    else:
        if [x for x in map_data[obj.x][obj.y+1] if x in obj_list]:
            return True
    return False


def look_print(obj, map_data, looks):
    check_list = map_look_list.look[f"{obj.x},{obj.y},{obj.obj_dir}"][str(looks)]
    for ls in check_list:
        map_data[ls["x"]][ls["y"]]["tmp"] = add_obj(ls["x"],ls["y"])


def check_front_around(obj, map_data, obj_list, looks):
    check_list = map_look_list.look[f"{obj.x},{obj.y},{obj.obj_dir}"][str(looks)]
    for ls in check_list:
        for key in obj_list:
            if key in map_data[ls["x"]][ls["y"]]:
                return True
    return False



def turn_target(target, obj):
    t_x = target.x
    t_y = target.y
    o_x = obj.x
    o_y = obj.y
    x_dis = abs(o_x-t_x)
    y_dis = abs(o_y-t_y)
    if y_dis>x_dis:
        if o_y-t_y>0:
            obj.obj_dir = 1
            obj.marker = "v"
        else:
            obj.obj_dir = 3
            obj.marker = "^"
    else:
        if o_x-t_x>0:
            obj.obj_dir = 2
            obj.marker = "<"
        else:
            obj.obj_dir = 0
            obj.marker = ">"


def get_target(obj, map_data, target, looks):
    check_list = map_look_list.look[f"{obj.x},{obj.y},{obj.obj_dir}"][str(looks)]
    for ls in check_list:
        if target in map_data[ls["x"]][ls["y"]]:
            return map_data[ls["x"]][ls["y"]][target]
    return False


def add_obj(x,y):
    return tmpObj(x,y)