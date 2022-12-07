

import rich

# ----------------------------------------------- constants------------------------------------------------- #

MAX_SIZE = 100000
TOTAL_SIZE = 70000000
REQ_SIZE = 30000000

# ----------------------------------------------- get input ----------------------------------------------- # 

with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

# ----------------------------------------------- directree ----------------------------------------------- # 


tree = {
    '/' : []
}

# ---------------------------------------------- parse input ---------------------------------------------- # 

curr = '/'

for line in raw_data:
    cmds = line.split()
    if cmds[0] == '$':
        match cmds[1]:
            case 'cd':
                if cmds[2] == '/':
                    curr = '/'

                elif cmds[2] == '..':
                    curr = '-'.join(curr.split('-')[:-1])

                else:
                    curr = curr + '-' + cmds[2]

            case 'ls':
                pass
    else:
        if cmds[0].isnumeric():
            tree[curr].append((cmds[1], int(cmds[0])))

        elif cmds[0] == "dir":
            tree[curr + '-' + cmds[1]] = []
            tree[curr].append(curr + '-' + cmds[1])

# -------------------------------------- calculate directory sizes ---------------------------------------- # 

size = {}

def get_size(dir):
    total = 0
    for sub_dir in tree[dir]:
        if type(sub_dir) != tuple:
            total += get_size(sub_dir)
        else:
            total += sub_dir[1]

    size[dir] = total
    return total

# ------------------------------------ print tree function for debugging ----------------------------------- # 

def printtree(dir, n = 0):
    if size[dir] > MAX_SIZE:
        rich.print('    ' * n, f"[bold red]{dir}[/bold red]")
    else:
        rich.print('    ' * n, f"[bold cyan]{dir}[/bold cyan]")
        
    for sub_dir in tree[dir]:
        if type(sub_dir) != tuple:
            printtree(sub_dir, n + 1)
        else:
            print('    ' * (n + 1), '-- ', sub_dir)

# ------------------------------------------------- part 1 ------------------------------------------------- #

solution_1 = 0
disk_size = get_size('/')

for dir, space in size.items():
    if space <= 100000:
        solution_1 += space

# ------------------------------------------------ part 2 -------------------------------------------------- #

unused_space = TOTAL_SIZE - disk_size
unused_dirs = []

for dir, space in size.items():
    if unused_space + space >= 30000000:
        unused_dirs.append(space)

solution_2 = min(unused_dirs)

# ----------------------------------------------- solution ------------------------------------------------- #

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# ---------------------------------------------------------------------------------------------------------- #
