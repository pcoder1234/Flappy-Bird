import pygame
from sys import exit
import random

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

running = True

# FPS Timer
clock = pygame.time.Clock()

# Score
score = 0

# Set up text
game_font = pygame.font.SysFont('Arial', 36, True)

# Set up bird
bird = pygame.image.load("bird.png")
bird_rect = bird.get_rect(center=(100, SCREEN_HEIGHT/2))
gravity = 0

# Set up background
bg = pygame.transform.scale(pygame.image.load("bg.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up pipe
pipe_up = pygame.transform.scale(pygame.image.load("pipe.png"), (100, 425))
# 2 pipes: 1 for top & 1 for bottom
pipe_down = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("pipe.png"), (100, 425)), 180)

# Pipe rects
pipe_up_rect = pipe_up.get_rect(midleft=(SCREEN_WIDTH, 0))
pipe_down_rect = pipe_down.get_rect(midleft=(SCREEN_WIDTH, SCREEN_HEIGHT))
pipe_speed = 5



# Draw function that draws all items into screen
def draw():
    screen.blit(bg, (0, 0))
    screen.blit(pipe_up, pipe_up_rect)
    screen.blit(pipe_down, pipe_down_rect)
    screen.blit(bird, bird_rect)
    screen.blit(score_text, ((SCREEN_WIDTH/2 - score_text.get_width()), 50))


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    score_text = game_font.render(str(score), True, "#FFFFFF", None)
    gameover_text = game_font.render("Game Over", True, '#FF0000', '#000000')
    
    # User Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        gravity = -5
    
    # Checking for collisions
    if bird_rect.centery <= 0:
        screen.blit(gameover_text, ((SCREEN_WIDTH/2 - score_text.get_width()), (SCREEN_HEIGHT/2 - score_text.get_height())))
        print("\n")
        print(f"You Lose!\nScore: {score}")
        print("\n")
        break
    
    elif bird_rect.centery >= SCREEN_HEIGHT:
        screen.blit(gameover_text, ((SCREEN_WIDTH/2 - score_text.get_width()), (SCREEN_HEIGHT/2 - score_text.get_height())))
        print("\n")
        print(f"You Lose!\nScore: {score}")
        print("\n")
        break
    
    elif bird_rect.colliderect(pipe_up_rect) or bird_rect.colliderect(pipe_down_rect):
        screen.blit(gameover_text, ((SCREEN_WIDTH/2 - score_text.get_width()), (SCREEN_HEIGHT/2 - score_text.get_height())))
        print("\n")
        print(f"You Lose!\nScore: {score}")
        print("\n")
        break
    
    else:
        pass
    
    pipe_up_rect.x -= pipe_speed
    pipe_down_rect.x -= pipe_speed
    
    if pipe_up_rect.right <= 0:
        pipe_up_rect.right = SCREEN_WIDTH
        pipe_up_rect.centery = random.randint(-150, 0)
    
    if pipe_down_rect.right <= 0:
        pipe_down_rect.right = SCREEN_WIDTH
        pipe_down_rect.centery = pipe_up_rect.centery + SCREEN_HEIGHT
    
    if pipe_up_rect.centerx == bird_rect.centerx:
        score += 1
    
    bird_rect.y += gravity
    
    gravity += 0.3
    
    # Draw all sprites
    draw()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()