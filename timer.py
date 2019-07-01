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
        self.timer += 1
        if self.timer == 200:
            return 200
            self.timer = 0