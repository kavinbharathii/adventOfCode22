
# ---------------------------------------------------- parse data ---------------------------------------------------- # 

with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()


def update(h, t, record = False):

    if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
        return

    else:
        if h[0] > t[0]:
            t[0] += 1

        if h[0] < t[0]:
            t[0] -= 1
        
        if h[1] > t[1]:
            t[1] += 1

        if h[1] < t[1]:
            t[1] -= 1

        if record:
            tail_pos.add(tuple(t))
        
        update(h, t)

# ------------------------------------------------------ part 1 ------------------------------------------------------ # 

head = [0, 0]
tail = [0, 0]

tail_pos = set()

for cmd in raw_data:
    dir, dist = cmd.split()
    dist = int(dist)

    for _ in range(dist):
        match dir:
            case 'R':
                head[0] += 1

            case 'L':
                head[0] -= 1

            case 'U':
                head[1] += 1

            case 'D':
                head[1] -= 1

        update(head, tail, True)

tail_pos.add((0, 0))
solution_1 = len(tail_pos)

# ------------------------------------------------------ part 2 ------------------------------------------------------ # 

knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

tail_pos = set()

for cmd in raw_data:
    dir, dist = cmd.split()
    dist = int(dist)

    for _ in range(dist):
        match dir:
            case 'R':
                knots[0][0] += 1

            case 'L':
                knots[0][0] -= 1

            case 'U':
                knots[0][1] += 1

            case 'D':
                knots[0][1] -= 1

        for i in range(len(knots) - 2):
            update(knots[i], knots[i + 1])

        update(knots[-2], knots[-1], True)

tail_pos.add((0, 0))
solution_2 = len(tail_pos)

# -------------------------------------------------------------------------------------------------------------------- # 

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# -------------------------------------------------------------------------------------------------------------------- # 
