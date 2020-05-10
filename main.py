from random import randint
from game import *

def create_points(limitsX, limitsY, quantity):
    points = []
    for x in range(0, quantity):
        posX = randint(limitsX[0], limitsX[1])
        posY = randint(limitsY[0], limitsY[1])
        points.append([posX, posY, []])
    return points

def algorithm(points, size):
    for x in range(0, size):
        for y in range(0, size):
            lowest_delta = (0, size*size)
            for p in range(len(points)):
                delta = abs (points[p][0] - x) + abs(points[p][1] - y)
                if delta < lowest_delta[1]:
                    lowest_delta = (p, delta)

            actual = points[lowest_delta[0]]
            changeX = x - actual[0]
            changeY = y - actual[1]
            actual[2].append((changeX, changeY))
    return points

def main():
    points = create_points([0, 500], [0, 500], 10)
    regions = algorithm(points, 500)
    window = pygame_init()
    drawPoints(regions, window)
    stayForever()
    return


if __name__ == "__main__":
    main()