import random

class wall:
    x = 0
    y = 0
    type = 'wall'
    obstacle = True
    marker = ','
    color = 'red'
    obj_id = 0

    def __init__(self, x, y, color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.obj_id = random.random()

    def update(self, map_data):
        pass
    
    def end(self, map_data):
        pass
