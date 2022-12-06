
with open("data.txt", "r") as file:
    buffer = file.readline()

# ------------------------------------------ Part 1 ------------------------------------------ #

solution_1 = 0

for i in range(len(buffer) - 4):
    if len(set(buffer[i:i + 4])) == 4:
        solution_1 = i + 4
        break

# ------------------------------------------ Part 2 ------------------------------------------ #

solution_2 = 0

for i in range(len(buffer) - 14):
    if len(set(buffer[i:i + 14])) == 14:
        solution_2 = i + 14
        break

# ------------------------------------------------------------------------------------------ #

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# ------------------------------------------------------------------------------------------ #
