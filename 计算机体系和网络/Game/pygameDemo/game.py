import pygame
import sys
 
from collections import defaultdict

# 初始化窗口
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
#  GRANT ALL PRIVILEGES ON *.* TO 'root'@'120.78.176.136' IDENTIFIED BY 'rootroot' WITH GRANT OPTION;
# 初始化背景
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
background_image = pygame.image.load('images/background.jpg')
 
while True:
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60) 
while True:
    screen.fill((192, 192, 192))
    pygame.display.update()
    clock.tick(60)



class Game:
    def __init__(self, 
                 caption, 
                 width, 
                 height, 
                 back_image_filename, 
                 frame_rate):
        self.background_image = \
            pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []


    def update(self):
        for o in self.objects:
            o.update()
    
    def draw(self):
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN, 
                                pygame.MOUSEBUTTONUP, 
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))
    
            self.handle_events()
            self.update()
            self.draw()
    
            pygame.display.update()
            self.clock.tick(self.frame_rate)