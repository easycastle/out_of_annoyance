import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("")

clock = pygame.time.Clock

running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get:
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()