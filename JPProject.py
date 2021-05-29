import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
#Initial circle
circle_x = 200
circle_y = 300
radius = 100
# Initial square
square_x = 500
square_y = 200
side_length = 200
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((173,216,230))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600), 5)
    # Circle movement and size
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            circle_x += 0.5
        if event.key == pygame.K_LEFT:
            circle_x -= 0.5
        if event.key == pygame.K_UP:
            circle_y -= 0.5
        if event.key == pygame.K_DOWN:
            circle_y += 0.5
        if event.key == pygame.K_F1:
            radius += 0.05
        if event.key == pygame.K_F2:
            radius -= 0.05
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
        if event.key == pygame.K_F6:
            square_x += 0.5
        if event.key == pygame.K_F5:
            square_x -= 0.5
        if event.key == pygame.K_F7:
            square_y -= 0.5
        if event.key == pygame.K_F8:
            square_y += 0.5
        if event.key == pygame.K_F3:
            side_length += 0.05
        if event.key == pygame.K_F4:
            side_length -= 0.05

    pygame.draw.rect(screen, (0, 0, 100), (square_x, square_y, side_length, side_length))

    if square_x >= 800-side_length:
        square_x = 800-side_length
    if square_x <= side_length:
        square_x = side_length
    if square_y >= 600-side_length:
        square_y = 600-side_length
    if square_y <= 0:
        square_y = 0

    def total_area():
        distance_formula = sqrt((circle_x-square_x)^2+(circle_x-square_x)^2)

    pygame.draw.circle(screen, (0, 0, 0), (circle_x + radius, circle_y), 5)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x - radius, circle_y), 5)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x, circle_y + radius), 5)
    pygame.draw.circle(screen, (0, 0, 0), (circle_x, circle_y - radius), 5)
    pygame.draw.circle(screen, (0, 0, 0), (square_x, square_y), 5)
    pygame.draw.circle(screen, (0, 0, 0), (square_x + side_length, square_y), 5)
    pygame.draw.circle(screen, (0, 0, 0), (square_x, square_y + side_length), 5)
    pygame.draw.circle(screen, (0, 0, 0), (square_x + side_length, square_y  + side_length), 5)


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F9:
            pygame.Surface.lock(screen)

    pygame.display.update()



