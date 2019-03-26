from pygame import font, Surface, display
font.init()

class Controls:
    def __init__(self, scr_w, scr_h, list):
        self.surface = Surface((scr_w, scr_h))
        self.font = font.Font(None, 32)
        self.list = list
        self.surface.set_alpha(150)
    def show(self):
        for x in range(0, len(self.list)):
            self.surface.blit(self.font.render(self.list[x], 1, (255, 255, 255)), (100, x*30 + 20))    