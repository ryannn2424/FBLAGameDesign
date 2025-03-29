import pygame
import math
from Elements.Button import Button

class TitleMenu():
  # Im so sorry
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.base_width = 960
        self.base_height = 540
        self.scale_x = self.screen_rect.width / self.base_width
        self.scale_y = self.screen_rect.height / self.base_height
        
        # Store base values for button
        self.base_button_width = 230
        self.base_button_height = 45
        self.base_button_x = self.base_width // 2 - self.base_button_width // 2
        self.base_button_y = self.base_height // 2

        # Load and scale logo
        self.base_logo_width = 400  # Adjust these values based on your logo
        self.base_logo_height = 200
        self.original_logo = pygame.image.load("Assets/UIElements/GameNameLogo.png")
        scaled_logo_width = int(self.base_logo_width * self.scale_x)
        scaled_logo_height = int(self.base_logo_height * self.scale_y)
        self.logo = pygame.transform.scale(self.original_logo, (scaled_logo_width, scaled_logo_height))
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.centerx = self.base_button_x + self.base_button_width // 2
        self.logo_rect.bottom = self.base_button_y - 20

        # Logo rotation properties
        self.rotation_angle = 0
        self.rotation_direction = 1
        self.max_rotation = 15
        self.rotation_speed = 0.5
        
        # Create scaled button
        scaled_width = int(self.base_button_width * self.scale_x)
        scaled_height = int(self.base_button_height * self.scale_y)
        scaled_x = int(self.base_button_x * self.scale_x)
        scaled_y = int(self.base_button_y * self.scale_y)
        
        self.startButton = Button("Assets/UIElements/Buttons/Button.png", 
                           scaled_x, scaled_y + scaled_height + 10, 
                           scaled_width, scaled_height, 
                           text="Start")
        self.startButton.action = self.start_game
        
        self.leaderboardButton = Button("Assets/UIElements/Buttons/Button.png",
                            scaled_x, scaled_y + (scaled_height + 10) * 2, 
                            scaled_width, scaled_height, 
                            text="Leaderboard")
        
        self.optionsButton = Button("Assets/UIElements/Buttons/Button.png",
                            scaled_x, scaled_y + (scaled_height + 10) * 3, 
                            scaled_width, scaled_height, 
                            text="Options")
        
        self.quitButton = Button("Assets/UIElements/Buttons/Button.png",
                            scaled_x, scaled_y + (scaled_height + 10) * 4, 
                            scaled_width, scaled_height, 
                            text="Quit")
        self.quitButton.action = pygame.quit
        
        # Add fade effect properties
        self.fade_surface = pygame.Surface((self.screen_rect.width, self.screen_rect.height))
        self.fade_surface.fill((0, 0, 0))
        self.fade_alpha = 255
        self.fade_start_time = pygame.time.get_ticks()
        self.fade_duration = 1000  # 1 second in milliseconds
        self.fading_out = False
        self.fade_out_callback = None  # Function to call when fade out completes

    def resize(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.scale_x = self.screen_rect.width / self.base_width
        self.scale_y = self.screen_rect.height / self.base_height
        
        # Rescale button
        scaled_width = int(self.base_button_width * self.scale_x)
        scaled_height = int(self.base_button_height * self.scale_y)
        scaled_x = int(self.base_button_x * self.scale_x)
        scaled_y = int(self.base_button_y * self.scale_y)
        
        self.startButton = Button("Assets/UIElements/Buttons/Button.png",
                           scaled_x, scaled_y,
                           scaled_width, scaled_height,
                           text="Start")
        self.startButton.action = self.start_game
        
        self.leaderboardButton = Button("Assets/UIElements/Buttons/Button.png",
                            scaled_x, scaled_y + scaled_height + 10,
                            scaled_width, scaled_height,
                            text="Leaderboard")
        
        self.optionsButton = Button("Assets/UIElements/Buttons/Button.png",
                            scaled_x, scaled_y + (scaled_height + 10) * 2,
                            scaled_width, scaled_height,
                            text="Options")
        
        self.quitButton = Button("Assets/UIElements/Buttons/Button.png",
                            scaled_x, scaled_y + (scaled_height + 10) * 3,
                            scaled_width, scaled_height,
                            text="Quit")

        # Rescale logo
        scaled_logo_width = int(self.base_logo_width * self.scale_x)
        scaled_logo_height = int(self.base_logo_height * self.scale_y)
        self.logo = pygame.transform.scale(self.original_logo, (scaled_logo_width, scaled_logo_height))
        self.logo_rect = self.logo.get_rect()
        self.logo_rect.centerx = scaled_x + scaled_width // 2
        self.logo_rect.bottom = scaled_y - 20
        
    def reset_fade(self):
        self.fade_start_time = pygame.time.get_ticks()
        self.fade_alpha = 255

    def start_fade_out(self, callback=None):
        self.fading_out = True
        self.fade_start_time = pygame.time.get_ticks()
        self.fade_alpha = 0
        self.fade_out_callback = callback

    def reset_fade_in(self):
        self.fading_out = False
        self.fade_start_time = pygame.time.get_ticks()
        self.fade_alpha = 255
        self.fade_out_callback = None
        
    def start_game(self):
        # Placeholder for starting the game
        print("Starting game...")
        self.start_fade_out()
        # pygame.quit()
    
    def draw(self):
        self.screen.fill((255, 255, 255))

        # Calculate the distance from the current angle to the max rotation
        distance_to_max = abs(self.max_rotation - abs(self.rotation_angle))

        # Adjust rotation speed based on a sine function
        normalized_distance = distance_to_max / self.max_rotation
        self.current_rotation_speed = self.rotation_speed * math.sin(normalized_distance * math.pi / 2)

        # Check if we've reached max rotation in either direction
        if self.rotation_angle >= self.max_rotation:
            self.rotation_direction = -1
        elif self.rotation_angle <= -self.max_rotation:
            self.rotation_direction = 1

        # Update rotation angle
        self.rotation_angle += self.current_rotation_speed * self.rotation_direction

        # Rotate and draw logo
        rotated_logo = pygame.transform.rotate(self.logo, self.rotation_angle)
        rotated_rect = rotated_logo.get_rect(center=self.logo_rect.center)
        self.screen.blit(rotated_logo, rotated_rect)

        if self.startButton.update():
            self.startButton.action()
        if self.leaderboardButton.update():
            self.leaderboardButton.action()
        if self.optionsButton.update():
            self.optionsButton.action()
        if self.quitButton.update():
            self.quitButton.action()
        
        self.screen.blit(self.startButton.image, self.startButton.rect)
        self.screen.blit(self.leaderboardButton.image, self.leaderboardButton.rect)
        self.screen.blit(self.optionsButton.image, self.optionsButton.rect)
        self.screen.blit(self.quitButton.image, self.quitButton.rect)

        # Handle fade effect
        current_time = pygame.time.get_ticks()
        elapsed = current_time - self.fade_start_time
        
        if elapsed < self.fade_duration:
            if self.fading_out:
                self.fade_alpha = int(255 * (elapsed / self.fade_duration))
            else:
                self.fade_alpha = int(255 * (1 - elapsed / self.fade_duration))
            self.fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(self.fade_surface, (0, 0))
        elif self.fading_out and self.fade_out_callback:
            self.fade_out_callback()
        
        pygame.display.flip()