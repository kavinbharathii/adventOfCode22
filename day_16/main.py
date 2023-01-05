
from collections import deque

with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

valves = {}
tunnels = {}

for line in raw_data:
    line = line.split()
    valve = line[1]
    flow = int(line[4].strip(';').split('=')[-1])
    targets = [x.strip().strip(',') for x in line[9:]]
    
    valves[valve] = flow
    tunnels[valve] = targets

dists = {}
non_empty = []

for valve in valves:
    if valve != "AA" and not valves[valve]:
        continue

    if valve != "AA":
        non_empty.append(valve)

    dists[valve] = {valve: 0, "AA": 0}
    visited = {valve}

    queue = deque([(0, valve)])

    while queue:
        distance, position = queue.popleft()
        for neighbor in tunnels[position]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if valves[neighbor]:
                dists[valve][neighbor] = distance + 1
            queue.append((distance + 1, neighbor))


    del dists[valve][valve]

    if valve != "AA":
        del dists[valve]["AA"]

indices = {}

for index, element in enumerate(non_empty):
    indices[element] = index

cache = {}

def dfs(time, valve, bitmask):

    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]

    max_value = 0

    for neighbor in dists[valve]:
        bit = 1 << indices[neighbor]
        if bitmask & bit:
            continue

        remtime = time - dists[valve][neighbor] - 1
        if remtime <= 0:
            continue

        max_value = max(max_value, dfs(remtime, neighbor, bitmask | bit) + valves[neighbor] * remtime)

    cache[(time, valve, bitmask)] = max_value
    return max_value

solution_1 = dfs(30, "AA", 0)

e = (1 << len(non_empty)) - 1
solution_2 = 0

for i in range((e + 1) // 2):
    solution_2 = max(solution_2, dfs(26, "AA", i) + dfs(26, "AA", e ^ i))

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")
