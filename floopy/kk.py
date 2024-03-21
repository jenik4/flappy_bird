import pygame
import sys
import random

pygame.init()

width = 800
height = 600
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("bINGbONG")
bg = pygame.image.load("floopy/bg.png")
bg = pygame.transform.scale(bg, (width, height))


white = (255, 255, 255)
black = (0, 0, 0)
paddle_color = (107, 60, 36)
ball_color = (255, 3, 3)

paddle_width = 9
paddle_height = height // 2
paddle_speed = 4
bottom_wall = pygame.Rect(50,0 , paddle_width, random.randint(250,400))
upper_wall = pygame.Rect(width, 0, paddle_width, random.randint(50, 300))
collision_sound = pygame.mixer.Sound("floopy/metal-pipe-clang.mp3")


ball_radius = 30
ball_speed_y = 2
ball_jump = 10
bird_img = pygame.image.load("floopy/ptak.png")
bird_img = pygame.transform.scale(bird_img, (ball_radius * 2, ball_radius * 2))
ball = bird_img.get_rect(center=(width // 2, height // 2))

player1_score = 0

font = pygame.font.Font(None, 36)



def update():
    global ball_speed_y, player1_score, bottom_wall, paddle_speed, upper_wall

    ball.y += ball_speed_y
    bottom_wall.x -= paddle_speed
    upper_wall.x -= paddle_speed

    if ball.top <= 0 or ball.bottom >= height:
        reset_ball()
        collision_sound.play()
        reset_wall()
        player1_score = 0


    if ball.colliderect(bottom_wall) or ball.colliderect(upper_wall):
        player1_score = 0
        paddle_speed = 4
        reset_ball()        
        collision_sound.play()
        reset_wall()


    if bottom_wall.left == width // 2 and height // 2:
        player1_score += 1

    if bottom_wall.left <= 0:
        reset_wall()

def reset_ball():
    global ball_speed_y
    ball.center = (width // 2, height // 2)

def reset_wall():
    global upper_wall, bottom_wall
    bottom_wall.center = (width, height)
    upper_wall = pygame.Rect(width, 0, paddle_width, random.randint(50, 300))

def draw():
    win.blit(bg, (0,0))
    pygame.draw.rect(win, paddle_color, bottom_wall)
    pygame.draw.rect(win, paddle_color, upper_wall)
    win.blit(bird_img, ball)
    score_text = font.render(f"{player1_score}", True, white)
    win.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and bottom_wall.top > 0:
            ball.y -= ball_jump

        update()
        draw()
        clock.tick(120)
        

if __name__ == "__main__":
    main()

