import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800 ,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the player")

clock = pygame.time.Clock()
FPS = 60

player_image = pygame.image.load('player1.png')
player_image = pygame.transform.scale(player_image, (50, 50))
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)
player_speed = 5

collect_image = pygame.image.load('pizza.png')
collect_image = pygame.transform.scale(collect_image, (30, 30))
collect_rect = collect_image.get_rect()
collect_rect.x = random.randint(0, WIDTH - collect_rect.width)
collect_rect.y = random.randint(0, HEIGHT - collect_rect.height)

score = 0
font = pygame.font.SysFont(None, 30)

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

    if player_rect.colliderect(collect_rect):
        score += 1
        collect_rect.x = random.randint(0, WIDTH - collect_rect.width)
        collect_rect.y = random.randint(0, HEIGHT - collect_rect.height)

    screen.fill((255,200,200))
    screen.blit(player_image, player_rect)
    screen.blit(collect_image, collect_rect)

    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

pygame.quit()