import pygame
import random
import math
import nature

def random_color():
    red = random.randint(10, 255)
    green = random.randint(10, 255)
    blue = random.randint(10, 255)
    return (red, green, blue)

class Blob():
    def __init__(self, screen_width, screen_height):
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        self.speed = random.randint(6, 30)
        self.angle = math.radians(random.random() * 360)
     
        self.color = random_color()
        
        radius = random.randint(5, 30)
        self.radius = radius
        
        self.x_min = radius
        self.x_max = screen_width - radius
        self.y_min = radius
        self.y_max = screen_height - radius 
        
        self.x = random.randint(self.x_min, self.x_max )
        self.y = random.randint(self.y_min, self.y_max)
        
        self.energy = nature.born_energy
    
    def update(self):
        self.angle += random.choice([-1, 1]) * random.random()
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        if(self.x < self.x_min or self.x > self.x_max or self.y < self.y_min or self.y > self.y_max):
            self.speed = -self.speed
        self.energy -= nature.energy_consume(self.speed, self.radius)
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        