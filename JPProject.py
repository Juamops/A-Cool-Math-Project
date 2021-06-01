import pygame
import math

screensize = (800,600)

pygame.init()
screen = pygame.display.set_mode(screensize)
# Mouse Control
clicking = False
click_loc = [-1, -1]

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

while running:

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Click Events
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicking = True
            click_loc = [mx, my]

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            clicking = False
            click_loc = [-1, -1]
    # Circle movement
    if clicking and distance(mx, my, circle_x, circle_y) <= radius:
        if mx >= radius and my >= radius and mx <= screensize[0] - radius and my <= screensize[1] - radius:
            circle_x = mx
            circle_y = my
    # Square movement      
    if clicking and distance(mx, my, center_square_x, center_square_y) <= radius:
        if mx >= side_length/2 and my >= side_length/2 and mx <= screensize[0] - side_length/2 and my <= screensize[1] - side_length/2:
            center_square_x = mx
            center_square_y = my

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

    pygame.draw.rect(screen, (0, 0, 100), (center_square_x-side_length/2, center_square_y-side_length/2, side_length, side_length))
    
    def total_area():
        distance_between_centers = math.sqrt((circle_x-square_x)**2+(circle_x-square_x)**2)
        """
        distance_between_pointoncircle_centersquare = distance_between_centers - radius 
        ratio = distance_between_pointoncircle_centersquare/distance_between_centers
        if distance_between_pointoncircle_centersquare <= 0:
            center of square inside
        elif distance_between_pointoncircle_centersquare >= 0:
            center of square outside
            
        if the center of square is outside, use ratio to create percentage, then subtract that percentage from the area of square-
        - then add area of circle to get total area.
        area of square = side_length^2 - (side_length^2 * ratio) 
        final area = radius^2 * pi + area of square
        
        if the center of the square is inside, 
        
        """

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

