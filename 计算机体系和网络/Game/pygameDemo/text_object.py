import pygame
 
 
class TextObject:
    def __init__(self, 
                 x, 
                 y, 
                 text_func, 
                 color, 
                 font_name, 
                 font_size):
        self.pos = (x, y)
        self.text_func = text_func
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)
        self.bounds = self.get_surface(text_func())
 
    def draw(self, surface, centralized=False):
        text_surface, self.bounds = \
            self.get_surface(self.text_func())
        if centralized:
            pos = (self.pos[0] - self.bounds.width // 2,
                   self.pos[1])
        else:
            pos = self.pos
        surface.blit(text_surface, pos)
 
    def get_surface(self, text):
        text_surface = self.font.render(text, 
                                        False, 
                                        self.color)
        return text_surface, text_surface.get_rect()
 
    def update(self):
        pass