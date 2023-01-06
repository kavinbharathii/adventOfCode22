
import re

with open("data.aoc", "r") as file:
    raw_data = [line.strip('\n') for line in file.readlines()]
    file.close()

dirs = raw_data[-1]
grid = raw_data[:-2]

max_width = max(len(line) for line in grid)
grid = [line + (" " * (max_width - len(line))) for line in grid]

r = 0
c = grid[0].index('.', 1)
dr = 0
dc = 1

for x, y in re.findall(r"(\d+)([RL]?)", dirs):
    x = int(x)

    for _ in range(x):
        cdr = dr
        cdc = dc
        nr = r + dr
        nc = c + dc
        if nr < 0 and 50 <= nc < 100 and dr == -1:
            dr, dc = 0, 1
            nr, nc = nc + 100, 0
        elif nc < 0 and 150 <= nr < 200 and dc == -1:
            dr, dc = 1, 0
            nr, nc = 0, nr - 100
        elif nr < 0 and 100 <= nc < 150 and dr == -1:
            nr, nc = 199, nc - 100
        elif nr >= 200 and 0 <= nc < 50 and dr == 1:
            nr, nc = 0, nc + 100
        elif nc >= 150 and 0 <= nr < 50 and dc == 1:
            dc = -1
            nr, nc = 149 - nr, 99
        elif nc == 100 and 100 <= nr < 150 and dc == 1:
            dc = -1
            nr, nc = 149 - nr, 149
        elif nr == 50 and 100 <= nc < 150 and dr == 1:
            dr, dc = 0, -1
            nr, nc = nc - 50, 99
        elif nc == 100 and 50 <= nr < 100 and dc == 1:
            dr, dc = -1, 0
            nr, nc = 49, nr + 50
        elif nr == 150 and 50 <= nc < 100 and dr == 1:
            dr, dc = 0, -1
            nr, nc = nc + 100, 49
        elif nc == 50 and 150 <= nr < 200 and dc == 1:
            dr, dc = -1, 0
            nr, nc = 149, nr - 100
        elif nr == 99 and 0 <= nc < 50 and dr == -1:
            dr, dc = 0, 1
            nr, nc = nc + 50, 50
        elif nc == 49 and 50 <= nr < 100 and dc == -1:
            dr, dc = 1, 0
            nr, nc = 100, nr - 50
        elif nc == 49 and 0 <= nr < 50 and dc == -1:
            dc = 1
            nr, nc = 149 - nr, 0
        elif nc < 0 and 100 <= nr < 150 and dc == -1:
            dc = 1
            nr, nc = 149 - nr, 50
        if grid[nr][nc] == "#":
            dr = cdr
            dc = cdc
            break
        r = nr
        c = nc
    if y == "R":
        dr, dc = dc, -dr
    elif y == "L":
        dr, dc = -dc, dr

dir_dict = {
    (0, 1)  : 0,
    (1, 0)  : 1,
    (0, -1) : 2,
    (-1, 0) : 3
}

solution_1 = 1000 * (r + 1) + 4 * (c + 1) + dir_dict[(dr, dc)]
print(f"Part 1: {solution_1}")

