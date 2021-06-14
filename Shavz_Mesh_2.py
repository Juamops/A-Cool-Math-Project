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
triangle_side_length = 25
# Button for area
circle_2_x = 60
circle_2_y = 60
radius_2 = 30

running = True


def distance(point_one, point_two):
    return ((point_one[0] - point_two[0]) ** 2 + (point_one[1] - point_two[1]) ** 2) ** 0.5


def within(point, square, sides):
    return square[0] <= point[0] <= square[0] + sides and square[1] <= point[1] <= square[1] + sides


def check_point(point_x, point_y):
    check = 0
    if square_x - 10 <= point_x <= (square_x + side_length + 10):
        check += 1
    if square_y - 10 <= point_y <= (square_y + side_length + 10):
        check += 1
    return check


def find_inside(circle, radius, square, sides, centers):
    inside = []
    for point in centers:
        if distance(point, circle) <= radius or within(point, square, sides):
            inside.append(point)
    return inside


def plot_vertices(centers, triangle_side_length):
    # Plots vertices clockwise starting at 12 o'clock
    points = []
    radius = ((triangle_side_length*(3**0.5)))/3
    for o in range(len(centers)):
        vertices = []
        #print(indexes[o])
        for i in range(3):
            if o % 2 == 0:
                degrees = (i * 120) - 90
            else:
                degrees = (i * 120) + 90

            vertices.append((round(((centers[o][0]) + (radius * math.cos(math.radians(degrees))))),
                            round((centers[o][1]) + (radius * math.sin(math.radians(degrees))))))
        points.append(vertices)

    return points


def get_lines(points):
    lines = []
    for hexagon in points:
        hex_lines = []
        for i in range(len(hexagon)):
            if i <= (len(hexagon) - 2):
                hex_lines.append((hexagon[i], hexagon[i + 1]))
            else:
                hex_lines.append((hexagon[i], hexagon[0]))

        lines.append(hex_lines)

    return lines


def triangle_grid():
    point_coordinate = []
    for y in range(round(screensize[1] / ((triangle_side_length / 2) * (3 ** 0.5)))):
        for x in range(round(screensize[0] / (triangle_side_length/3))):
            if x % 2 == 0:
                point_coordinate.append((round(x*(triangle_side_length/2)), round(((triangle_side_length * (3**0.5))/6) + (y*((triangle_side_length)*(3**0.5))/2))))
            else:
                point_coordinate.append((round(x * (triangle_side_length/2)), round((y * ((triangle_side_length) * (3 ** 0.5)) / 2))))

    inside_points = find_inside((circle_x, circle_y), radius, (square_x, square_y), side_length, point_coordinate)

    print(inside_points)
    vertices = plot_vertices(inside_points, triangle_side_length)
    #print(vertices)
    triangle_lines = get_lines(vertices)

    print(vertices)

    for triangle in triangle_lines:
        for vertex in triangle:
            pygame.draw.line(screen, (255, 255, 255), vertex[0], vertex[1], 1)
    """
    faces = 0
    for point in point_coordinate:
        for target in point_coordinate:
            for second_target in point_coordinate:
                if (point[1] + target[1] + second_target[1]) / 3 != point[1]:
                    if triangle_side_length == round(distance(point[0], point[1], target[0], target[1])) == round(
                            distance(target[0], target[1], second_target[0], second_target[1])) == round(
                            distance(point[0], point[1], second_target[0], second_target[1])):
                        faces += 1
    """
    #area = (faces / 6) * ((triangle_side_length ** 2) * ((3 ** 0.5) / 4))
    #print(faces/6)



while running:

    screen.fill((173, 216, 230))

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
    if clicking and distance((mx, my), (circle_x, circle_y)) <= radius:
        if mx >= radius and my >= radius and mx <= screensize[0] - radius and my <= screensize[1] - radius:
            circle_x = mx
            circle_y = my

    # Square movement
    if clicking and distance((mx, my), (center_square_x, center_square_y)) <= radius:
        if mx >= side_length / 2 and my >= side_length / 2 and mx <= screensize[0] - side_length / 2 and my <= \
                screensize[1] - side_length / 2:
            center_square_x = mx
            center_square_y = my

    if right_clicking and distance((mx, my), (circle_x, circle_y)) <= radius:
        radius = round(distance((mx, my), (circle_x, circle_y))) + 2

    # Square movement and Sizing
    if clicking and within((mx, my), (square_x, square_y), side_length):
        if mx >= side_length / 2 and my >= side_length / 2 and mx <= screensize[0] - side_length / 2 and my <= \
                screensize[1] - side_length / 2:
            square_x = round(mx - (side_length / 2))
            square_y = round(my - (side_length / 2))

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

    triangle_grid()


    pygame.display.update()