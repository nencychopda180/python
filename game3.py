import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Shooting Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player
player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 7

# Bullet
bullet_width, bullet_height = 5, 10
bullet_speed = 10
bullets = []

# Target
target_width, target_height = 50, 50
targets = []
target_speed = 3
spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, 1500)  # Spawn target every 1.5 seconds

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_event:
            x = random.randint(0, WIDTH - target_width)
            y = -target_height
            targets.append(pygame.Rect(x, y, target_width, target_height))
    
    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 5:  # Limit bullets on screen
            bullets.append(pygame.Rect(player_x + player_width//2 - bullet_width//2, player_y, bullet_width, bullet_height))
    
    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)
    
    # Move targets
    for target in targets[:]:
        target.y += target_speed
        if target.y > HEIGHT:
            targets.remove(target)
    
    # Check collision
    for bullet in bullets[:]:
        for target in targets[:]:
            if bullet.colliderect(target):
                bullets.remove(bullet)
                targets.remove(target)
                score += 1
                break
    
    # Draw player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
    
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    
    # Draw targets
    for target in targets:
        pygame.draw.rect(screen, BLUE, target)
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
