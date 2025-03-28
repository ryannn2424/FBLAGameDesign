import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height, action=None, text=None):
        super().__init__()
        self.font = pygame.font.Font('Assets/UIElements/Font/DepartureMonoNerdFont-Regular.otf', 36)
        
        # Create a default surface if image loading fails
        loaded_image = self.load_image(image)
        if loaded_image is None:
            self.image = pygame.Surface((width, height))
            self.image.fill((200, 200, 200))  # Grey background as fallback
        else:
            self.image = pygame.transform.scale(loaded_image, (width, height))
            
        # Center the button at the given coordinates
        self.rect = self.image.get_rect(center=(x, y))
        self.action = action
        
        if text:
            self.draw_text(text)

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

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if self.action:
                    self.action()