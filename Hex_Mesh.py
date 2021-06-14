import math


def distance(point_one, point_two):
    return ((point_one[0] - point_two[0]) ** 2 + (point_one[1] - point_two[1]) ** 2) ** 0.5


def within(point, square, sides):
    return square[0] <= point[0] <= square[0] + sides and square[1] <= point[1] <= square[1] + sides


def plot_centers(radius, screensize):
    centers = []
    for x in range(round(screensize[0] / (radius * math.cos(math.radians(30))))):
        for y in range(round(screensize[1] / (radius + (math.sin(math.radians(30)))))):
            if y % 2 == 0:
                centers.append(
                    (round((radius * math.cos(math.radians(30))) + (x * 2 * (radius * math.cos(math.radians(30))))),
                     round(radius + (y * (radius + (radius * math.sin(math.radians(30))))))))
            elif y % 2 == 1:
                centers.append(((x * 2 * (radius * math.cos(math.radians(30)))),
                                radius + (y * (radius + (radius * math.sin(math.radians(30)))))))

    return centers


def plot_vertices(centers, radius):
    # Plots vertices clockwise starting at 12 o'clock
    points = []
    for center in centers:
        vertices = []
        for i in range(6):
            degrees = (i * 60) - 90
            vertices.append(((center[0]) + (radius * math.cos(math.radians(degrees))),
                             (center[1]) + (radius * math.sin(math.radians(degrees)))))
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


def find_inside(circle, radius, square, sides, centers):
    inside = []
    for point in centers:
        if distance(point, circle) <= radius or within(point, square, sides):
            inside.append(point)
    return inside


def get_area(centers, radius):
    return centers * (6 * (radius ** 2 * ((3 ** 0.5) / 4)))
