import pygame

pygame.init()

WIDTH, HEIGHT = 400 ,300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the player")

clock = pygame.time.Clock()
FPS = 60

player_size = 30
player_color = (0, 100, 255)
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    screen.fill((255,200,200))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    pygame.display.flip()

pygame.quit()