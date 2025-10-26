import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600 ,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Pizza")

clock = pygame.time.Clock()
FPS = 60

player_image = pygame.image.load('player1.png')
player_image = pygame.transform.scale(player_image, (50, 50))
player_rect = player_image.get_rect()
player_rect.midbottom = (WIDTH // 2, HEIGHT - 10)
player_speed = 7

collect_image = pygame.image.load('pizza.png')
collect_image = pygame.transform.scale(collect_image, (30, 30))
falling_pizza = []

for _ in range(3):
    x = random.randint(0, WIDTH - 30)
    y = random.randint(-300, -50)
    falling_pizza.append(pygame.Rect(x, y, 30, 30))

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


    player_rect.x = max(0, min(WIDTH - player_rect.width, player_rect.x))

    for pizza in falling_pizza:
        pizza.y += 2
        if pizza.y > HEIGHT:
            pizza.y = random.randint(-300, -50)
            pizza.x = random.randint(0, WIDTH - pizza.width)

        if player_rect.colliderect(pizza):
            score += 1
            pizza.y = random.randint(-300, -50)
            pizza.x = random.randint(0, WIDTH - pizza.width)

    screen.fill((255,200,200))
    screen.blit(player_image, player_rect)
    for pizza in falling_pizza:
        screen.blit(collect_image, pizza)

    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

pygame.quit()