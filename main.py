import pygame
from blob import Blob
import nature

pygame.init()

screen = pygame.display.set_mode((nature.world_width, nature.world_height))

pygame.display.set_caption("Blobs")

clock = pygame.time.Clock()

running = True

blobs = []
for i in range(50):
    blob = Blob(screen.get_width(), screen.get_height())
    blobs.append(blob)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
     
    screen.fill( (0, 0, 0))
    
    for b in blobs:
        if(b.energy > 0):
            b.update()
            b.draw(screen)
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
    