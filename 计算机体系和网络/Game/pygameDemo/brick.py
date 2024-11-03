""" Drawing Bricks

Bricks are bricks. They are just rectangles. Pygame provides the pygame.draw.rect() function, which takes a surface, a color, and a Rect object (left, top, width and height) and renders a rectangle. If the optional width parameter is greater than zero, it draws the outline. If the width is zero (which is the default), it draws a solid rectangle.

Note that the Brick class is a subclass of GameObject and gets all its properties, but it also has a color it manages itself (because there may be game objects that don't have a single color). Ignore the special_effect field for now. """
import pygame
 
from game_object import GameObject
 
 
class Brick(GameObject):
    def __init__(self, x, y, w, h, color, special_effect=None):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.special_effect = special_effect
 
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)