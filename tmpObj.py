import random

class tmpObj:
    x = 0
    y = 0
    type = 'tmp'
    obstacle = True
    marker = 'x'
    color = 'blue'
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.obj_id = random.random()
    
    def update(self, map_data):
        pass
    
    def end(self, map_data):
        del map_data[self.x][self.y]["tmp"]
        del self