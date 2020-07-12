import random
import agent

class people:
    x = 0
    y = 0
    type = 'people'
    obstacle = True
    marker = '.'
    color = 'blue'
    add_x = 0
    add_y = 0
    obj_id = 0
    # 0:右　1:下　2:左　3:上
    obj_dir = 0

    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.add_x = 1
        self.add_y = 1
        self.obj_dir = 0
        self.obj_id = random.random()

    def update(self, map_data):
        if agent.check_front(self, map_data, ["wall", "people", "chase"]):
            if random.random() > 0.5:
                agent.turn(self, 1)
            else:
                agent.turn(self, -1)
            if not agent.check_front(self, map_data, ["people", "wall", "chase"]):
                agent.move_front(self, map_data, 1)
        else:
            if random.random() > 0.5:
                if random.random() > 0.5:
                    agent.turn(self, 1)
                else:
                    agent.turn(self, -1)
            if not agent.check_front(self, map_data, ["people", "wall", "chase"]):
                agent.move_front(self, map_data, 1)
    
    def end(self, map_data):
        pass
        

def get_dis(target, obj):
    return abs(obj.x - target.x) + abs(obj.y - target.y)