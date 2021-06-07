import pygame
import math

screensize = (800,600)

pygame.init()
screen = pygame.display.set_mode(screensize)
# Mouse Control
clicking = False
right_clicking = False
click_loc = [-1, -1]
starting_size = 0

#Initial circle
circle_x = 200
circle_y = 300
radius = 100
# Initial square
square_x = 500
square_y = 200
side_length = 200
center_square_x = square_x + side_length/2
center_square_y = square_y + side_length/2
running = True

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def within (mx, my, x, y, width, height):
    return (mx >= x and mx <= x + width and my >= y and my <= y + height)

while running:

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Click Events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
                click_loc = [mx, my]
            if event.button == 3:
                right_clicking = True
                starting_size = side_length

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False
                click_loc = [-1, -1]
            if event.button == 3:
                right_clicking = False

    # Circle movement and Sizing
    if clicking and distance(mx, my, circle_x, circle_y) <= radius:
        if mx >= radius and my >= radius and mx <= screensize[0] - radius and my <= screensize[1] - radius:
            circle_x = mx
            circle_y = my

    # Square movement      
    if clicking and distance(mx, my, center_square_x, center_square_y) <= radius:
        if mx >= side_length/2 and my >= side_length/2 and mx <= screensize[0] - side_length/2 and my <= screensize[1] - side_length/2:
            center_square_x = mx
            center_square_y = my


    if right_clicking and distance(mx, my, circle_x, circle_y) <= radius:
        radius = round(distance(mx, my, circle_x, circle_y)) + 2
    
    # Square movement and Sizing
    if clicking and within(mx, my, square_x, square_y, side_length, side_length):
        if mx >= side_length / 2 and my >= side_length / 2 and mx <= screensize[0] - side_length / 2 and my <= \
                screensize[1] - side_length / 2:
            square_x = round(mx - (side_length / 2))
            square_y = round(my - (side_length / 2))

    """
    Will Hopefully Work Soon!
    if right_clicking and within(mx, my, square_x, square_y, side_length, side_length):
        side_length = starting_size - (click_loc[1] - my)
    """


    screen.fill((173,216,230))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600), 5)
    # Circle movement and size

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            radius += 1
        if event.key == pygame.K_RIGHT:
            radius -= 1

    pygame.draw.circle(screen, (0, 0, 100), (circle_x, circle_y), radius)
    if circle_x >= 800 - radius:
        circle_x = 800 - radius
    if circle_x <= radius:
        circle_x = radius
    if circle_y >= 600 - radius:
        circle_y = 600 - radius
    if circle_y <= radius:
        circle_y = radius

    #Square movement and size
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            side_length += 1
        if event.key == pygame.K_DOWN:
            side_length -= 1
            square_y += 0.5
        if event.key == pygame.K_F3:
            side_length += 0.05
        if event.key == pygame.K_F4:
            side_length -= 0.05


    pygame.draw.rect(screen, (0, 0, 100), (center_square_x-side_length/2, square_y, side_length, side_length))
    if square_x >= 800-side_length:
        square_x = 800-side_length
    if square_x <= side_length:
        square_x = side_length
    if square_y >= 600-side_length:
        square_y = 600-side_length
    if square_y <= 0:
        square_y = 0

    pygame.draw.rect(screen, (0, 0, 100), (center_square_x-side_length/2, center_square_y-side_length/2, side_length, side_length))

    pygame.draw.circle(screen, (0, 0, 0), (circle_x + radius, circle_y), 5)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x - radius, circle_y), 5)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x, circle_y + radius), 5)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x, circle_y - radius), 5)
    pygame.draw.circle(screen, (0, 0, 0), (center_square_x-side_length/2, center_square_y-side_length/2), 5)
    pygame.draw.circle(screen, (0, 0, 0), (center_square_x+side_length/2, center_square_y-side_length/2), 5)
    pygame.draw.circle(screen, (0, 0, 0), (center_square_x-side_length/2, center_square_y+side_length/2), 5)
    pygame.draw.circle(screen, (0, 0, 0), (center_square_x+side_length/2, center_square_y+side_length/2), 5)


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F9:
            pygame.Surface.lock(screen)

    pygame.display.update()

