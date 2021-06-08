import pygame
import math
screen_x = 800
screen_y = 600
screensize = (screen_x, screen_y)

pygame.init()
screen = pygame.display.set_mode(screensize)
# Mouse Control
clicking = False
right_clicking = False
click_loc = [-1, -1]
starting_size = 0

# Initial circle
circle_x = 200
circle_y = 300
radius = 100
# Initial square
square_x = 500
square_y = 200
side_length = 200
center_square_x = square_x + side_length / 2
center_square_y = square_y + side_length / 2
# Triangle side length
triangle_side_length = 15
running = True


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def within(mx, my, x, y, width, height):
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
        if mx >= side_length / 2 and my >= side_length / 2 and mx <= screensize[0] - side_length / 2 and my <= \
                screensize[1] - side_length / 2:
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

    screen.fill((173, 216, 230))
    #pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600), 5)
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

    # Square movement and size
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

    pygame.draw.rect(screen, (0, 0, 100), (center_square_x - side_length / 2, square_y, side_length, side_length))
    if square_x >= 800 - side_length:
        square_x = 800 - side_length
    if square_x <= side_length:
        square_x = side_length
    if square_y >= 600 - side_length:
        square_y = 600 - side_length
    if square_y <= 0:
        square_y = 0

    pygame.draw.rect(screen, (0, 0, 100),(center_square_x - side_length / 2, center_square_y - side_length / 2, side_length, side_length))

    pygame.draw.circle(screen, (0, 0, 0), (circle_x + radius, circle_y), 5)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x - radius, circle_y), 5)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x, circle_y + radius), 5)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x, circle_y - radius), 5)
    pygame.draw.circle(screen, (0, 0, 0), (center_square_x - side_length / 2, center_square_y - side_length / 2), 5)
    pygame.draw.circle(screen, (0, 0, 0), (center_square_x + side_length / 2, center_square_y - side_length / 2), 5)
    pygame.draw.circle(screen, (0, 0, 0), (center_square_x - side_length / 2, center_square_y + side_length / 2), 5)
    pygame.draw.circle(screen, (0, 0, 0), (center_square_x + side_length / 2, center_square_y + side_length / 2), 5)

    def check_point(point_x,point_y):
        check = 0
        if square_x <= point_x <= (square_x + side_length):
            check += 1
        if square_y <= point_y <= (square_y + side_length):
            check += 1
        return check

    def triangle_grid():
        x = 0
        y = 0

        points = 0
        while y <= 600:
            while x <= 800:
                pygame.draw.circle(screen, (0, 0, 0), (x, y), 1)
                if distance(x,y,circle_x,circle_y) <= radius or distance(x,y,circle_x,circle_y) == radius:
                    points += 1
                elif check_point(x,y) == 2:
                    points += 1
                else:
                    pygame.draw.circle(screen, (173, 216, 230), (x, y), 1)
                x += triangle_side_length
            x = 0 + triangle_side_length / 2
            y += triangle_side_length/(2**0.5)
            while x <= 800:
                pygame.draw.circle(screen, (0, 0, 0), (x, y), 1)
                if distance(x,y,circle_x,circle_y) <= radius or distance(x,y,circle_x,circle_y) == radius:
                    points += 1
                elif check_point(x, y) == 2:
                    points += 1
                else:
                    pygame.draw.circle(screen, (173, 216, 230), (x, y), 1)
                x += triangle_side_length
            x = 0
            y += triangle_side_length/(2**0.5)
            while x <= 800:
                pygame.draw.circle(screen, (0, 0, 0), (x, y), 1)
                if distance(x,y,circle_x,circle_y) <= radius or distance(x,y,circle_x,circle_y) == radius:
                    points += 1
                elif check_point(x,y) == 2:
                    points += 1
                else:
                    pygame.draw.circle(screen, (173, 216, 230), (x, y), 1)
                x += triangle_side_length
        print(points)

    triangle_grid()

    pygame.display.update()
