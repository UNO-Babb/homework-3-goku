import pygame


pygame.init()


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Move Goku Around")


goku = pygame.image.load("goku.gif")  # Make sure the file path is correct
goku_rect = goku.get_rect()
goku_rect.topleft = (50, 50)  # Starting position


clock = pygame.time.Clock()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_LEFT]:
        goku_rect.x -= 5  # Move Goku left
    if keys[pygame.K_RIGHT]:
        goku_rect.x += 5  # Move Goku right
    if keys[pygame.K_UP]:
        goku_rect.y -= 5  # Move Goku up
    if keys[pygame.K_DOWN]:
        goku_rect.y += 5  # Move Goku down

    
    if goku_rect.left < 0:
        goku_rect.left = 0
    if goku_rect.right > 600:
        goku_rect.right = 600
    if goku_rect.top < 0:
        goku_rect.top = 0
    if goku_rect.bottom > 600:
        goku_rect.bottom = 600

    
    screen.fill((255, 255, 255))  # White background

    
    screen.blit(goku, goku_rect)

    
    pygame.display.flip()

    
    clock.tick(60)

# Quit Pygame
pygame.quit()
