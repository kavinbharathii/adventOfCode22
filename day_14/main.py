
# ---------------------------------------------------- parse input ---------------------------------------------------- #

with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()


sand_source = (500, 0)

path_vecs = []

for line in raw_data:
    path_vecs.append([])
    for coords in line.split(' -> '):
        x, y = coords.split(',')
        path_vecs[-1].append((int(x), int(y)))

min_x = max_x = 500
min_y = max_y = 0

for path in path_vecs:
    for coord in path:
        if coord[0] < min_x:
            min_x = coord[0]

        if coord[0] > max_x:
            max_x = coord[0]

        if coord[1] < min_y:
            min_y = coord[1] 

        if coord[1] > max_y:
            max_y = coord[1] 

rocks = set()

for path in path_vecs:
    for i in range(1, len(path)):
        if path[i - 1][0] == path[i][0]:
            min_index = min(path[i][1], path[i - 1][1])
            max_index = max(path[i][1], path[i - 1][1])
            for r in range(min_index, max_index + 1):
                rocks.add((path[i][0], r))

        elif path[i - 1][1] == path[i][1]:
            min_index = min(path[i][0], path[i - 1][0])
            max_index = max(path[i][0], path[i - 1][0])
            for r in range(min_index, max_index + 1):
                rocks.add((r, path[i][1]))

visual_grid = []
grid = []

for j in range(min_y, max_y + 1):
    visual_grid.append([])
    grid.append([])
    for i in range(min_x, max_x + 1):
        if (i, j) in rocks:
            visual_grid[-1].append('#')
            grid[-1].append(2)
        elif (i, j) == sand_source:
            visual_grid[-1].append('+')
            grid[-1].append(0)
        else:
            visual_grid[-1].append('.')
            grid[-1].append(0)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if visual_grid[i][j] == '+': sand_source = (i, j)


def dropsand(sand_source):
    # Initialize position as the block below the SOURCE block, and check the three options
    # (1, 0), (1, -1) and (1, 1) until the sand particle becomes blocked.
    pos = [sand_source[0], sand_source[1]]

    # If the source is blocked [required for part 2]
    if grid[sand_source[0] + 1][sand_source[1]] != 0 and grid[sand_source[0] + 1][sand_source[1] - 1] != 0 and grid[sand_source[0] + 1][sand_source[1] + 1] != 0:
        return True
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
            break

    grid[pos[0]][pos[1]] = 1
    return False

# ------------------------------------------------------ part one ------------------------------------------------------ #


solution_1 = 0

while True:
    try:
        dropsand(sand_source)
    except:
        total = 0
        for i in grid:
            for j in i:
                if j == 1: total += 1

        solution_1 = total
        break

# ------------------------------------------------------ part two ------------------------------------------------------ #


visual_grid = []
grid = []

sand_source = (500, 0)

for j in range(min_y, max_y + 1):
    visual_grid.append([])
    grid.append([])
    for i in range(min_x - max_y, max_x + max_y + 1):
        if (i, j) in rocks:
            visual_grid[-1].append('#')
            grid[-1].append(2)
        elif (i, j) == sand_source:
            visual_grid[-1].append('+')
            grid[-1].append(1)
        else:
            visual_grid[-1].append('.')
            grid[-1].append(0)


# adding the goddamn floor
grid.append([0] * len(grid[0]))
grid.append([2] * len(grid[0]))

# adding the goddamn floor to visual
visual_grid.append(['.'] * len(grid[0]))
visual_grid.append(['#'] * len(grid[0]))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if visual_grid[i][j] == '+': 
            sand_source = (i, j)

solution_2 = 0

while True:
    res = dropsand(sand_source)
    if res:
        break

for i in grid:
    for j in i:
        if j == 1:
            solution_2 += 1
# # ---------------------------------------------------------------------------------------------------------------------- #

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# ---------------------------------------------------------------------------------------------------------------------- #
