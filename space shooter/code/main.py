import pygame

# general setup - initilizing the game / display scfeen
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# plain surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

#importing an image 

player_surf = pygame.image.load('../images/player.png')

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('darkgrey')
    x += 0.1
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()


pygame.quit()