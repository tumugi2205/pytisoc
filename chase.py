import random
import agent

class chase:
    x = 0
    y = 0
    type = 'chase'
    obstacle = True
    marker = '>'
    color = 'yellow'
    add_x = 0
    add_y = 0
    obj_id = 0
    # 0:右　1:下　2:左　3:上
    obj_dir = 0
    flag = 0

    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.add_x = 1
        self.add_y = 1
        self.obj_dir = 0
        self.obj_id = random.random()
        self.flag = 0

    def update(self, map_data):
        self.color = "red"
        if agent.check_front_around(self, map_data, ["people"], 9):
            self.color = "yellow"
            agent.turn_target(agent.get_target(self, map_data, "people", 9), self)
            if not agent.check_front(self, map_data, ["people", "wall", "chase"]):
                agent.move_front(self, map_data, 1)
        elif agent.check_front(self, map_data, ["wall"]):
            if random.random() > 0.5:
                agent.turn(self, 1)
            else:
                agent.turn(self, -1)
            if not agent.check_front(self, map_data, ["people", "wall", "chase"]):
                agent.move_front(self, map_data, 1)
        else:
            if random.random() > 0.8:
                if random.random() > 0.5:
                    agent.turn(self, 1)
                else:
                    agent.turn(self, -1)
            if not agent.check_front(self, map_data, ["people", "wall", "chase"]):
                agent.move_front(self, map_data, 1)
        # agent.look_print(self, map_data, 9)
    
    def end(self, map_data):
        pass