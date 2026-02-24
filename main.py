# |---- Main imports   ------------
import pygame


# |---- Own imports   ------------
from source.scripts import display


# |---- Main code    ------------
# |------------------------------
# |---- Starts PyGame -----------
pygame.init()

# |---- Draws the screen and gives the title of it ------------
game_screen = pygame.display.set_mode((display.default_width, display.default_height))
pygame.display.set_caption("Last ashes of The Morning")

ingame_clock = pygame.time.Clock()
isit_running = True

while isit_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isit_running = False

    game_screen.fill(display.default_background)

    # CODE


    pygame.display.flip()
    ingame_clock.tick(30)

pygame.quit()