
from collections import deque

with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]  
    file.close()

drops = set()
offsets = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
solution_1 = 0

minx = miny = minz = 10e6
maxx = maxy = maxz = -10e6

for line in raw_data:
    x, y, z = map(int, line.split(','))
    drops.add((x, y, z))

    minx = min(minx, x)
    miny = min(miny, y)
    minz = min(minz, z)

    maxx = max(maxx, x)
    maxy = max(maxy, y)    
    maxz = max(maxz, z)


for drop in drops:
    x, y, z = drop
    for dx, dy, dz in offsets:
        cell = (x + dx, y + dy, z + dz)
        if cell not in drops:
            solution_1 += 1

minx -= 1
miny -= 1
minz -= 1

maxx += 1
maxy += 1
maxz += 1


air = {(minx, miny, minz)}
queue = deque([(minx, miny, minz)])

while queue:
    x, y, z = queue.popleft()

    for dx, dy, dz in offsets:
        nx = x + dx
        ny = y + dy
        nz = z + dz

        cell = (nx, ny, nz)

        if not ((minx <= nx <= maxx) and (miny <= ny <= maxy) and (minz <= nz <= maxz)):
            continue
    
        if cell in drops or cell in air:
            continue

        air.add(cell)
        queue.append(cell)

solution_2 = 0

for (x, y, z) in drops:
    for dx, dy, dz in offsets:
        if (x + dx, y + dy, z + dz) in air:
            solution_2 += 1


print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

