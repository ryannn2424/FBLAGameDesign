import pygame
from Elements.Button import Button


class TitleMenu():
  def __init__(self, screen):
    self.screen = screen
    self.screen_rect = self.screen.get_rect()
    self.button = Button("Assets/UIElements/Buttons/Button.png", self.screen_rect.centerx, self.screen_rect.centery, 250, 50, text="Start")
    
  def draw(self):
    self.screen.fill((255, 255, 255))
    self.button.update()
    self.screen.blit(self.button.image, self.button.rect)
    pygame.display.flip()