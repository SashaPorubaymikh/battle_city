class Timer:
    def __init__(self):
        self.timer = 199
    def update(self):
        self.timer += 1
        if self.timer == 200:
            self.timer = 0
            return True