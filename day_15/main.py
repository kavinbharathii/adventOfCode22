

import rich

with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

sensors = []
beacons = []
visited = set()

Y = 20_00_000
# Y = 10

def manhattan(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return abs(x1 - x2) + abs(y1 - y2)

for line in raw_data:
    line = line.split()
    sx, sy = int(line[2].split('=')[-1].strip(',')), int(line[3].split('=')[-1].strip(':'))
    bx, by = int(line[-2].split('=')[-1].strip(',')), int(line[-1].split('=')[-1])

    sensors.append((sx, sy))
    beacons.append((bx, by))

def visit_beacon(s, b, optimized = True):
    (sx, sy), (bx, by) = s, b
    dist = manhattan((sx, sy), (bx, by))

    start_x = sx - dist
    end_x = sx + dist + 1

    start_y = sy - dist
    end_y = sy + dist + 1

    if optimized:
        if start_y <= Y <= end_y:
            sub = abs(start_y - Y)
            for c in range(start_x + abs(dist - sub), end_x - abs(dist - sub)):
                if (c, Y) not in sensors and (c, Y) not in beacons:
                    visited.add((c, Y))

    else:
        sub = 0
        for r in range(start_y, end_y):
            for c in range(start_x + abs(dist - sub), end_x - abs(dist - sub)):
                if (c, r) not in sensors and (c, r) not in beacons:
                    visited.add((c, r))
            sub += 1

def print_grid(gx, gy):
    rich.print("      " + " ".join([str(abs(i)).zfill(2)[0] if str(abs(i)).zfill(2)[0] != '0' else ' ' for i in range(gx, gy)]))
    rich.print("      " + " ".join([str(abs(i)).zfill(2)[1] for i in range(gx, gy)]))

    for i in range(gx, gy):
        rich.print(f"{' ' * (3 - len(str(i)))}{i}: ", end = " ")
        for j in range(gx, gy):

            if (j, i) in sensors:
                rich.print("[bold red]S[/bold red]", end = " ")

            elif (j, i) in beacons:
                rich.print("[bold blue]B[/bold blue]", end = " ")

            elif (j, i) in visited:
                rich.print(".", end = " ")

            else:
                rich.print(' ', end = ' ')

        print()


for s, b in zip(sensors, beacons):
    visit_beacon(s, b)

# print_grid(-10, 30)

total = 0
for _, y in visited:
    if y == Y:
        total += 1

print(f"Part 1: {total}")


pos_lines = []
neg_lines = []

for i, (s, b) in enumerate(zip(sensors, beacons)):
    d = manhattan(s, b)
    neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
    pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])


pos = None
neg = None

for i in range(2 * len(sensors)):
    for j in range(i + 1, 2 * len(sensors)):
        a, b = pos_lines[i], pos_lines[j]

        if abs(a - b) == 2:
            pos = min(a, b) + 1

        a, b = neg_lines[i], neg_lines[j]

        if abs(a - b) == 2:
            neg = min(a, b) + 1

x, y = (pos + neg) // 2, (neg - pos) // 2
solution_2 = x * 4000000 + y
print(f"Part 2: {solution_2}")