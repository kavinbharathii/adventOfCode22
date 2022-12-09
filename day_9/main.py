
# ---------------------------------------------------- parse data ---------------------------------------------------- # 

with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()


# Update the tail based on the head

def update(h, t, record = False):

    # If they are touching, don't do anything
    if abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
        return

    else:
        if h[0] > t[0]:             # if the head is above the tail in x axis
            t[0] += 1               # increment the tail by one in x axis

        if h[0] < t[0]:             # if the head is below the tail in x axis
            t[0] -= 1               # decrement the tail by one in x axis
        
        if h[1] > t[1]:             # if the head is after the tail in y axis
            t[1] += 1               # increment the tail by one in y axis

        if h[1] < t[1]:             # if the head is before the tail in y axis
            t[1] -= 1               # decrement the tail by one in y axis


        # If we are recording the moves [to account for the second problem],
        # record it once the movement is complete. Since the x and y are dealt seperately 
        # and the record is taken AFTER the movement, the diagonal rule is satisfied
        if record:
            tail_pos.add(tuple(t))
        
        # Recursively update the tail until it's touching the head [atmost for 2 depth, I think]
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

knots = [[0, 0] for _ in range(10)]

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
