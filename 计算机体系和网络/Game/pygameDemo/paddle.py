""" Drawing the Paddle
The paddle is yet another rectangle that is indeed moving left and right in response to the player's pressing the arrow keys. That means that the position of the paddle may change from one frame to the next, but as far as drawing goes, it is just a rectangle that has to be rendered at the current position, whatever that is.  """
import pygame
 
import config as c
from game_object import GameObject
 
 
class Paddle(GameObject):
    def __init__(self, x, y, w, h, color, offset):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.offset = offset
        self.moving_left = False
        self.moving_right = False
 
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)