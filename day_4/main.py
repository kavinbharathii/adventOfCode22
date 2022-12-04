
with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

total_score = 0

# ---------------------------------------- part 1 ---------------------------------------- #

for data in raw_data:
    a_range, b_range = data.split(',')
    a_range = list(range(int(a_range.split('-')[0]), int(a_range.split('-')[1]) + 1))
    b_range = list(range(int(b_range.split('-')[0]), int(b_range.split('-')[1]) + 1))

    a_set = set(a_range)
    b_set = set(b_range)

    if a_set.union(b_set) == a_set or b_set.union(a_set) == b_set:
        total_score += 1

solution_1 = total_score 

# ---------------------------------------- part 1 ---------------------------------------- #

total_score = 0

for data in raw_data:
    a_range, b_range = data.split(',')
    a_range = list(range(int(a_range.split('-')[0]), int(a_range.split('-')[1]) + 1))
    b_range = list(range(int(b_range.split('-')[0]), int(b_range.split('-')[1]) + 1))

    a_set = set(a_range)
    b_set = set(b_range)

    if a_set.intersection(b_set):
        total_score += 1

solution_2 = total_score 

# --------------------------------------------------------------------------------------- #

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")
