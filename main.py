import pygame
import sys
import os

import TitleMenu

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

# Store window sizes
WINDOW_SIZES = {
    "windowed": (960, 540),
    "fullscreen": (1920, 1080)
}

# Initialize screen with flags
screen = pygame.display.set_mode(WINDOW_SIZES["windowed"])
pygame.display.set_caption("FBLA Game Design")

# Cursor
# pygame.mouse.set_visible(False)
# cursor = pygame.image.load("Assets/UIElements/Cursor/Player1Cursor.png")
# cursor = pygame.transform.scale(cursor, (38, 32)) 
# cursor_rect = cursor.get_rect()
cursor_surface = pygame.transform.scale(pygame.image.load("Assets/UIElements/Cursor/Player1Cursor.png"), (38, 32))
hotspot = (0,0)
cursor = pygame.cursors.Cursor(hotspot, cursor_surface)
pygame.mouse.set_cursor(cursor)

# Title Menu
titleMenu = TitleMenu.TitleMenu(screen)
titleMenu.reset_fade_in()

# Main game loop
running = True
isFullscreen = False
clock = pygame.time.Clock()

while running:
    # Lock to 144 FPS
    clock.tick(144)
    
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                isFullscreen = not isFullscreen
                if isFullscreen:
                    screen = pygame.display.set_mode(WINDOW_SIZES["fullscreen"], pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
                else:
                    screen = pygame.display.set_mode(WINDOW_SIZES["windowed"])
                # Update title menu's screen reference
                titleMenu = TitleMenu.TitleMenu(screen)
    
    # Draw Title Menu
    titleMenu.draw()
    
    # Draw cursor last
    # cursor_rect.center = pygame.mouse.get_pos()
    # screen.blit(cursor, cursor_rect.topleft)
    
    pygame.display.flip()

pygame.quit()
sys.exit()