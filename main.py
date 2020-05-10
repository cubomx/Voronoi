from random import randint


def create_points(limitsX, limitsY, quantity):
    points = []
    for x in range(0, quantity):
        posX = randint(limitsX[0], limitsX[1])
        posY = randint(limitsY[0], limitsY[1])
        points.append((posX, posY))
    return points


def main():
    print(create_points([0, 100], [0, 100], 10))
    return


if __name__ == "__main__":
    main()