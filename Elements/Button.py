import pygame
import math

class Button(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height, action=None, text=None):
        super().__init__()
        self.font = pygame.font.Font('Assets/UIElements/Font/DepartureMonoNerdFont-Regular.otf', math.floor((height - 10) * 0.72))
        self.image = pygame.transform.scale(self.load_image(image), (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action
        self.text = text

    def load_image(self, image_path):
        try:
            image = pygame.image.load(image_path).convert_alpha()
            return image
        except pygame.error as e:
            print(f"Error loading image: {e}")
            return None
          
    def draw_text(self, text):
        text_surface = self.font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.rect.width//2, self.rect.height//2))
        self.image.blit(text_surface, text_rect)

    def hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = pygame.transform.scale(self.load_image("Assets/UIElements/Buttons/ButtonSelected.png"), self.rect.size)
        else:
            self.image = pygame.transform.scale(self.load_image("Assets/UIElements/Buttons/Button.png"), self.rect.size)
        if self.text: 
            self.draw_text(self.text)


    def update(self):
        self.hover()
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
              # print(f'Button {self} clicked')
              if self.action:
                  print('actionewd')
                  self.action()