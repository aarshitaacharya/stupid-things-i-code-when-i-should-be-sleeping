import pygame

pygame.init()

WIDTH, HEIGHT = 400 ,300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the player")

clock = pygame.time.Clock()
FPS = 60

player_image = pygame.image.load('player.png')
player_image = pygame.transform.scale(player_image, (40, 32))
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)
player_speed = 5

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    player_rect.x = max(0, min(WIDTH - player_rect.width, player_rect.x))
    player_rect.y = max(0, min(HEIGHT - player_rect.height, player_rect.y))

    screen.fill((255,200,200))
    screen.blit(player_image, player_rect)
    pygame.display.flip()

pygame.quit()