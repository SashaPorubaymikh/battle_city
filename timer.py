class Timer:
    def __init__(self):
        self.timer = 0
    def update(self):
        self.timer += 1
        if self.timer == 200:
            self.timer = 0
            return True

class New_timer:
    def __init__(self):
        self.time = 0
    def update(self):
        self.time += 1
        if self.time == 215:
            return True
            self.time = 0