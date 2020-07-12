import json
dic = {}
x_loop = [1,0,-1,0]
y_loop = [0,-1,0,1]
for y in range(50):
    for x in range(50):
        for dirs in range(4):
            dic[f"{x},{y},{dirs}"] = {}
            for z in range(10):
                ls = []
                for di in range(z):
                    i=di+1
                    start_x = x_loop[dirs]
                    start_y = y_loop[dirs]
                    if start_x == 1:
                        dx = start_x+i+x
                        if i == z:
                            if dx<0 or dx>50:
                                pass
                            else:
                                ls.append({"x":dx-1,"y":y})
                        for dy in range(-z+i,z-i+1):
                            if dy+y<0 or dy+y>50 or dx<0 or dx>50:
                                pass
                            else:
                                ls.append({"x":dx-1,"y":dy+y})
                    elif start_x == -1:
                        dx = start_x-i+x
                        if i == z:
                            if dx<0 or dx>50:
                                pass
                            else:
                                ls.append({"x":dx+1,"y":y})
                        for dy in range(-z+i,z-i+1):
                            if dy+y<0 or dy+y>50 or dx<0 or dx>50:
                                pass
                            else:
                                ls.append({"x":dx+1,"y":dy+y})            
                    elif start_y == 1:
                        dy = start_y+i+y                    
                        if i == z:
                            if dy<0 or dy>50:
                                pass
                            else:
                                ls.append({"x":x,"y":dy-1})
                        for dx in range(-z+i,z-i+1):
                            if dx+x<0 or dx+x>50 or dy<0 or dy>50:
                                pass
                            else:
                                ls.append({"x":dx+x,"y":dy-1})
                    elif start_y == -1:
                        dy = start_y-i+y
                        if i == z:
                            if dy<0 or dy>50:
                                pass
                            else:
                                ls.append({"x":x,"y":dy+1})
                        for dx in range(-z+i,z-i+1):
                            if dx+x<0 or dx+x>50 or dy<0 or dy>50:
                                pass
                            else:
                                ls.append({"x":dx+x,"y":dy+1})
                dic[f"{x},{y},{dirs}"][f"{z}"] = ls
with open("look.json", mode="w") as f:
    json.dump(dic,f,indent=2)