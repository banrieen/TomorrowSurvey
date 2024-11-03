""" Drawing the Ball

The ball in Breakout is just a circle. Pygame provides the pygame.draw.circle() function that takes the color, center, radius and the options width parameter that defaults to zero. As with the pygame.draw.rect() function, if the width is zero then a solid circle is drawn. The Ball is also a derived class of GameObject. 

Since the ball is always moving (unlike the bricks), it also has a speed that is passed on the GameObject base class to be managed. The Ball class has a little twist because its x and y parameters denote its center, while the x and y parameters passed to the GameObject base class are the top-left corner of the bounding box. To convert from center to top-left corner, all it takes is subtracting the radius.  """

import pygame
 
from game_object import GameObject
 
 
class Ball(GameObject):
    def __init__(self, x, y, r, color, speed):
        GameObject.__init__(self, 
                            x - r, 
                            y - r, 
                            r * 2, 
                            r * 2, 
                            speed)
        self.radius = r
        self.diameter = r * 2
        self.color = color
 
    def draw(self, surface):
        pygame.draw.circle(surface, 
                           self.color, 
                           self.center, 
                           self.radius)