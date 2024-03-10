import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Snake properties
snake_block = 10
snake_speed = 20

# Clock to control frame rate
clock = pygame.time.Clock()

# Font for displaying messages
font = pygame.font.SysFont(None, 30)

# Draw snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(dis, green, [block[0], block[1], snake_block, snake_block])

# Display message
def message(msg, color):
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

# Game loop
def gameLoop():
    game_over = False
    snake_list = [[dis_width/2, dis_height/2]]
    snake_length = 1
    x_change = 0
    y_change = 0
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if snake_list[-1][0] >= dis_width or snake_list[-1][0] < 0 or snake_list[-1][1] >= dis_height or snake_list[-1][1] < 0:
            game_over = True

        snake_list[-1][0] += x_change
        snake_list[-1][1] += y_change

        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        draw_snake(snake_block, snake_list)

        pygame.display.update()

        if snake_list[-1][0] == foodx and snake_list[-1][1] == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
