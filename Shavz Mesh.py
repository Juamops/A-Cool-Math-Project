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
# Triangle and hexagon side length
triangle_side_length = 15
hexagonal_side_length = 15
# Button for area
circle_2_x = 60
circle_2_y = 60
radius_2 = 30


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

    pygame.draw.circle(screen, (0, 0, 200), (circle_2_x, circle_2_y), radius_2)
    pygame.draw.circle(screen, (0, 0, 100), (circle_x, circle_y), radius)
    pygame.draw.line(screen, (0,0,0), (0,110), (800,110), 4)

    if circle_x >= 800 - radius:
        circle_x = 800 - radius
    if circle_x <= radius:
        circle_x = radius
    if circle_y >= 600 - radius:
        circle_y = 600 - radius
    if circle_y <= 110 + radius:
        circle_y = 110 + radius

    # Square movement and size
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            side_length += 1
            square_y -= 0.5
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
        y = 115

        triangle_points = 0
        point_coordinate = []
        while y <= 600:
            while x <= 800:
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)
                if distance(x,y,circle_x,circle_y) <= radius or distance(x,y,circle_x,circle_y) == radius:
                    triangle_points += 1
                    point_coordinate.append((x, y))
                elif check_point(x,y) == 2:
                    triangle_points += 1
                    point_coordinate.append((x, y))
                else:
                    pygame.draw.circle(screen, (173, 216, 230), (x, y), 1)
                x += triangle_side_length
            x = 0 + triangle_side_length / 2
            y += triangle_side_length/(2**0.5)
            while x <= 800:
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)
                if distance(x,y,circle_x,circle_y) <= radius or distance(x,y,circle_x,circle_y) == radius:
                    triangle_points += 1
                    point_coordinate.append((x, y))
                elif check_point(x, y) == 2:
                    triangle_points += 1
                    point_coordinate.append((x, y))
                else:
                    pygame.draw.circle(screen, (173, 216, 230), (x, y), 1)
                x += triangle_side_length
            x = 0
            y += triangle_side_length/(2**0.5)
            while x <= 800:
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 1)
                if distance(x,y,circle_x,circle_y) <= radius or distance(x,y,circle_x,circle_y) == radius:
                    triangle_points += 1
                    point_coordinate.append((x, y))
                elif check_point(x,y) == 2:
                    triangle_points += 1
                    point_coordinate.append((x, y))
                else:
                    pygame.draw.circle(screen, (173, 216, 230), (x, y), 1)
                x += triangle_side_length

        for point in point_coordinate:
            for target in point_coordinate:
                print((point,target))
                if distance(point[0], point[1], target[0], target[1]) == side_length:

                    print('yes')
                    pygame.draw.line(screen, (255, 255, 255), (point[0], point[1]), (target[0], target[1]), 1)

        #print(points)
        #print(point_coordinate)

    # Still working on hexagonal grid
    def hexagonal_grid():
        hexagonal_x = 0
        hexagonal_y = 115

        hexagonal_points = 0
        while hexagonal_y <= 600:
            while hexagonal_x <= 800:
                pygame.draw.circle(screen, (255, 255, 255), (hexagonal_x, hexagonal_y), 1)
                if distance(hexagonal_x,hexagonal_y,circle_x,circle_y) <= radius or distance(hexagonal_x,hexagonal_y,circle_x,circle_y) == radius:
                    hexagonal_points += 1
                elif check_point(hexagonal_x,hexagonal_y) == 2:
                    hexagonal_points += 1
                else:
                    pygame.draw.circle(screen, (173, 216, 230), (hexagonal_x, hexagonal_y), 1)
                hexagonal_x += hexagonal_side_length
            hexagonal_x = 0 + triangle_side_length / 2
            hexagonal_y += triangle_side_length/(2**0.5)
            while hexagonal_x <= 800:
                pygame.draw.circle(screen, (255, 255, 255), (hexagonal_x, hexagonal_y), 1)
                if distance(hexagonal_x,hexagonal_y,circle_x,circle_y) <= radius or distance(hexagonal_x,hexagonal_y,circle_x,circle_y) == radius:
                    hexagonal_points += 1
                elif check_point(hexagonal_x, hexagonal_y) == 2:
                    hexagonal_points += 1
                else:
                    pygame.draw.circle(screen, (173, 216, 230), (hexagonal_x, hexagonal_y), 1)
                hexagonal_x += hexagonal_side_length*2
            hexagonal_x = 0
            hexagonal_y += triangle_side_length/(2**0.5)
            while hexagonal_x <= 800:
                pygame.draw.circle(screen, (255, 255, 255), (hexagonal_x, hexagonal_y), 1)
                if distance(hexagonal_x,hexagonal_y,circle_x,circle_y) <= radius or distance(hexagonal_x,hexagonal_y,circle_x,circle_y) == radius:
                    hexagonal_points += 1
                elif check_point(hexagonal_x,hexagonal_y) == 2:
                    hexagonal_points += 1
                else:
                    pygame.draw.circle(screen, (173, 216, 230), (hexagonal_x, hexagonal_y), 1)
                hexagonal_x += hexagonal_side_length
    #hexagonal_grid()

    if clicking and distance(mx, my, circle_2_x, circle_2_y) <= radius:
        triangle_grid()

    pygame.display.update()
