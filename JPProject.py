import pygame
import math
import Hex_Mesh as hex

screensize = (800,600)

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

# Meshing
mesh_def = 5
hex_points = hex.plot_centers(mesh_def, screensize)

# Initial square
square_x = 500
square_y = 200
side_length = 200
center_square_x = square_x + side_length/2
center_square_y = square_y + side_length/2
running = True


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def within(mouse_x, mouse_y, x, y, width, height):
    return x <= mouse_x <= x + width and y <= mouse_y <= y + height


while running:
    screen.fill((173, 216, 230))

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Lock Screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F9:
                pygame.Surface.lock(screen)

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
    if clicking and not within(mx, my, square_x, square_y, side_length, side_length):
        if clicking and distance(mx, my, circle_x, circle_y) <= radius:
            if radius <= mx <= screensize[0] - radius and radius <= my <= screensize[1] - radius:
                circle_x = mx
                circle_y = my

    if right_clicking and distance(mx, my, circle_x, circle_y) <= radius:
        radius = round(distance(mx, my, circle_x, circle_y)) + 5

    # Square movement and Sizing
    if clicking and distance(mx, my, circle_x, circle_y) >= radius:
        if clicking and within(mx, my, square_x, square_y, side_length, side_length):
            if side_length / 2 <= mx <= screensize[0] - side_length / 2 and side_length / 2 <= my <= screensize[1]\
                    - side_length / 2:
                square_x = round(mx - (side_length / 2))
                square_y = round(my - (side_length / 2))


    # Drawing

    pygame.draw.circle(screen, (0, 0, 100), (circle_x, circle_y), radius)
    pygame.draw.rect(screen, (0, 0, 100), (square_x, square_y, side_length, side_length))

    inside = hex.find_inside(
        circle=(circle_x, circle_y),
        radius=radius,
        square=(square_x, square_y),
        sides=side_length,
        centers=hex_points)

    area = hex.get_area(len(inside), mesh_def)
    print(area)

    hex_lines = hex.get_lines(hex.plot_vertices(inside, mesh_def))

    for hexagon in hex_lines:
        for line in hexagon:
            pygame.draw.line(screen, (255, 255, 255), line[0], line[1], 1)

    pygame.display.update()

