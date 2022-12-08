
# ---------------------------------------------------- parse data ---------------------------------------------------- # 

with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

grid = [[int(i) for i in line] for line in raw_data]

# ------------------------------------------------------ part 1 ----------------------------------------------------- # 

solution_1 = len(grid) * 2 + (len(grid[0]) - 2) * 2
visibles = set()

for i in range(1, len(grid) - 1):
    max_tree = grid[i][0]
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] > max_tree:
            visibles.add((i, j))
            max_tree = grid[i][j]

for i in range(1, len(grid) - 1):
    max_tree = grid[i][-1]
    for j in range(len(grid[0]) - 1, 0, -1):
        if grid[i][j] > max_tree:
            visibles.add((i, j))
            max_tree = grid[i][j]


for j in range(1, len(grid[0]) - 1):
    max_tree = grid[0][j]
    for i in range(1, len(grid) - 1):
        if grid[i][j] > max_tree:
            visibles.add((i, j))
            max_tree = grid[i][j]

for j in range(1, len(grid[0]) - 1):
    max_tree = grid[-1][j]
    for i in range(len(grid) - 1, 0, -1):
        if grid[i][j] > max_tree:
            visibles.add((i, j))
            max_tree = grid[i][j]

solution_1 += len(visibles)

# ------------------------------------------------------ part 2 ----------------------------------------------------- # 

all_scenic_scores = []

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid) - 1):
        left = j - 1
        right = j + 1
        top = i - 1
        bottom = i + 1

        lt = rt = tt = bt = 1
        tree = grid[i][j]

        while left > 0:
            if grid[i][left] >= tree:
                break
            lt += 1
            left -= 1

        while right < len(grid[i]) - 1:
            if grid[i][right] >= tree:
                break
            rt += 1
            right += 1

        while top > 0:
            if grid[top][j] >= tree:
                break
            tt += 1
            top -= 1

        while bottom < len(grid) - 1:
            if grid[bottom][j] >= tree:
                break
            bt += 1
            bottom += 1

        tree_score = lt * rt * tt * bt
        all_scenic_scores.append(tree_score)

solution_2 = max(all_scenic_scores)

# ------------------------------------------------------------------------------------------------------------------ # 

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# ------------------------------------------------------------------------------------------------------------------ # 
