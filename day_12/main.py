
from collections import deque

# ---------------------------------------------------- parse input ---------------------------------------------------- #

with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()



grid = []

for i in raw_data:
    grid.append(i)

edges = []

for row in raw_data:
    edges.append([])
    for i in row:
        if i == 'S':
            edges[-1].append(1)
        elif i == 'E':
            edges[-1].append(26)
        else:
            edges[-1].append(ord(i) - ord('a') + 1)

# ------------------------------------------------------ part one ------------------------------------------------------ #

def search():
    q = deque()
    for r in range(len(edges)):
        for c in range(len(edges[0])):
            if edges[r][c] == 1 and grid[r][c] == 'S':
                q.append(((r, c), 0))


    visited = set()
    while q:
        (r, c), d = q.popleft()

        if (r, c) in visited:
            continue

        visited.add((r, c))

        if grid[r][c] == 'E':
            return d

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r + dr
            cc = c + dc
        
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and edges[rr][cc] <= edges[r][c] + 1:
                q.append(((rr, cc), d + 1))

solution_1 = search()

# ------------------------------------------------------ part two ------------------------------------------------------ #

def search():
    q = deque()
    for r in range(len(edges)):
        for c in range(len(edges[0])):
            if edges[r][c] == 1:
                q.append(((r, c), 0))


    visited = set()
    while q:
        (r, c), d = q.popleft()

        if (r, c) in visited:
            continue

        visited.add((r, c))

        if grid[r][c] == 'E':
            return d

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r + dr
            cc = c + dc
        
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[0]) and edges[rr][cc] <= edges[r][c] + 1:
                q.append(((rr, cc), d + 1))

solution_2 = search()

# ---------------------------------------------------------------------------------------------------------------------- #

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# ---------------------------------------------------------------------------------------------------------------------- #
