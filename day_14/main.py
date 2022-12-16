
# ---------------------------------------------------- parse input ---------------------------------------------------- #

with open("test.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

# ------------------------------------------------------ part one ------------------------------------------------------ #

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

grid = []

for j in range(min_y, max_y + 1):
    grid.append([])
    for i in range(min_x, max_x + 1):
        if (i, j) in rocks:
            grid[-1].append('#')
        elif (i, j) == sand_source:
            grid[-1].append('+')
        else:
            grid[-1].append('.')

for i in grid:
    print(" ".join(i))


# ------------------------------------------------------ part two ------------------------------------------------------ #



# ---------------------------------------------------------------------------------------------------------------------- #

# print(f"Print 1: {solution_1}")
# print(f"Print 2: {solution_2}")

# ---------------------------------------------------------------------------------------------------------------------- #
