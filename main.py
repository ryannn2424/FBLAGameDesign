import pygame
import sys
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption("FBLA Game Design")

# Main game loop
running = True
isFullscreen = False

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_F11:
        if isFullscreen == False:
          pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
        else:
          pygame.display.set_mode((960, 540))
        isFullscreen = not isFullscreen
        
  screen.fill((0, 0, 0))

  pygame.display.flip()

pygame.quit()
sys.exit()