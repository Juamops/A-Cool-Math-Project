import math
import random as rand


class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def can_grow(self, circle_center, radius, square, sides, circles):

        for circle in circles:
            if distance(circle.center, self.center) >= circle.radius + self.radius:
                return False

        if self.center[0] + self.radius >= square[0] + sides or self.center[0] - self.radius <= square[0]:
            if self.center[1] + self.radius >= square[1] + sides or self.center[1] - self.radius <= square[1]:
                return False

        if distance(self.center, circle_center) + self.radius >= radius:
            return False

        return True

    def grow(self, increment=1):
        self.radius += increment


def distance(point_one, point_two):
    return ((point_one[0] - point_two[0]) ** 2 + (point_one[1] - point_two[1]) ** 2) ** 0.5


def within(point, square, sides):
    return square[0] <= point[0] <= square[0] + sides and square[1] <= point[1] <= square[1] + sides


def random_point(circles, square, sides):
    point = (0, 0)
    found = False
    while not found:
        point = (rand.randint(square[0], square[0]+sides), rand.randint(square[1], square[1]+sides))
        for circle in circles:
            if distance(circle.center, point) >= circle.radius:
                found = True
                break

    return point


def run(n_circles, circle_center, radius, square, sides):

    default_circle = Circle(circle_center, 1)
    circles = [default_circle]

    while default_circle.can_grow(circle_center, radius, square, sides, circles):
        default_circle.grow()

    for i in range(n_circles - 1):
        circle = Circle(random_point(circles, square, sides), 1)
        while circle.can_grow(circle_center, radius, square, sides, circles):
            circle.grow()
        circles.append(circle)