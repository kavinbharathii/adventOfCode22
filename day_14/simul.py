
# -------------------------------------------------------- pygame -------------------------------------------------------- #
import pygame
from copy import deepcopy 

rez = 4 

DARK = (20, 20, 20)
LIGHT = (220, 220, 220)
SAND = (238, 232, 170)
BLOCK = (50, 50, 50)

# -------------------------------------------------------- read input -------------------------------------------------------- #

grid = []
source = None

with open("out.txt") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

for i in range(len(raw_data)):
    grid.append([])
    line = raw_data[i].split(' ')

    for j in range(len(line)):
        if line[j] == '#':
            cell = 2
        elif line[j] == '+':
            source = (i, j)
        else:
            cell = 0

        grid[-1].append(cell)

width = len(grid[0]) * rez
height = len(grid) * rez

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sand simulation")

# -------------------------------------------------------- read input -------------------------------------------------------- #

def draw_grid():
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if (j, i) == source:
                pygame.draw.rect(display, SAND, (i * rez, j * rez, rez, rez), 1)
            elif grid[j][i] == 1:
                pygame.draw.rect(display, SAND, (i * rez, j * rez, rez, rez))
            elif grid[j][i] == 2:
                pygame.draw.rect(display, BLOCK, (i * rez, j * rez, rez, rez))
            else:
                pygame.draw.rect(display, DARK, (i * rez, j * rez, rez, rez), 1)


def dropsand():
    # Initialize position as the block below the SOURCE block, and check the three options
    # (1, 0), (1, -1) and (1, 1) until the sand particle becomes blocked.
    pos = [source[0], source[1]]
    while True:
        if grid[pos[0] + 1][pos[1]] == 0:
            pos[0] += 1

        elif grid[pos[0] + 1][pos[1] - 1] == 0:
            pos[0] += 1
            pos[1] -= 1

        elif grid[pos[0] + 1][pos[1] + 1] == 0:
            pos[0] += 1
            pos[1] += 1

        else:
            total = 0
            for i in grid:
                for j in i:
                    if j == 1: total += 1

            print(total)
            break

    grid[pos[0]][pos[1]] = 1


def main():
    loop = True
    clock = pygame.time.Clock()
    while loop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                # quit()

        dropsand()
        draw_grid()
        pygame.display.flip()


if __name__ == "__main__":
    main()
