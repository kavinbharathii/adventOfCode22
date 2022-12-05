
# Crates input

# [N]             [R]             [C]
# [T] [J]         [S] [J]         [N]
# [B] [Z]     [H] [M] [Z]         [D]
# [S] [P]     [G] [L] [H] [Z]     [T]
# [Q] [D]     [F] [D] [V] [L] [S] [M]
# [H] [F] [V] [J] [C] [W] [P] [W] [L]
# [G] [S] [H] [Z] [Z] [T] [F] [V] [H]
# [R] [H] [Z] [M] [T] [M] [T] [Q] [W]
#  1   2   3   4   5   6   7   8   9 

with open("data.txt", "r") as file:
    cmds = [line.strip() for line in file.readlines()]
    file.close()

# -------------------------------------------------- part 1 -------------------------------------------------- # 
data = [
    ['N', 'T', 'B', 'S', 'Q', 'H', 'G', 'R'],
    ['J', 'Z', 'P', 'D', 'F', 'S', 'H'],
    ['V', 'H', 'Z'],
    ['H', 'G', 'F', 'J', 'Z', 'M'],
    ['R', 'S', 'M', 'L', 'D', 'C', 'Z', 'T'],
    ['J', 'Z', 'H', 'V', 'W', 'T', 'M'],
    ['Z', 'L', 'P', 'F', 'T'],
    ['S', 'W', 'V', 'Q'],
    ['C', 'N', 'D', 'T', 'M', 'L', 'H', 'W']
]

for cmd in cmds:
    cmd = cmd.split()
    quantity, fc, tc = int(cmd[1]), int(cmd[3]), int(cmd[5])
    
    for _ in range(quantity):
        crate = data[fc - 1].pop(0)
        data[tc - 1].insert(0, crate)

solution_1 = ''

for i in data:
    solution_1 += i[0]

# -------------------------------------------------- part 2 -------------------------------------------------- #

data = [
    ['N', 'T', 'B', 'S', 'Q', 'H', 'G', 'R'],
    ['J', 'Z', 'P', 'D', 'F', 'S', 'H'],
    ['V', 'H', 'Z'],
    ['H', 'G', 'F', 'J', 'Z', 'M'],
    ['R', 'S', 'M', 'L', 'D', 'C', 'Z', 'T'],
    ['J', 'Z', 'H', 'V', 'W', 'T', 'M'],
    ['Z', 'L', 'P', 'F', 'T'],
    ['S', 'W', 'V', 'Q'],
    ['C', 'N', 'D', 'T', 'M', 'L', 'H', 'W']
]

for cmd in cmds:
    cmd = cmd.split()
    quantity, fc, tc = int(cmd[1]), int(cmd[3]), int(cmd[5])
    
    crates = data[fc - 1][:quantity]
    data[fc - 1] = data[fc - 1][quantity:]
    data[tc - 1] = crates + data[tc - 1]

solution_2 = ''

for i in data:
    solution_2 += i[0]

# ------------------------------------------------------------------------------------------------------------ #

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# ------------------------------------------------------------------------------------------------------------ #
