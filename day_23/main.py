
with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

elves = set()

for r, line in enumerate(raw_data):
    for c, item in enumerate(line):
        if item == "#":
            elves.add(c + r * 1j)

scan_map = {
    -1j : [- 1 - 1j , -1j,  1 - 1j],
     1j : [-1 + 1j  , 1j ,  1 + 1j],
     -1 : [- 1 - 1j , -1 , -1 + 1j],
      1 : [1 - 1j   , 1  ,  1 + 1j]
}

moves = [-1j, 1j, -1, 1]
offsets = [-1 - 1j, -1j, -1j + 1, 1, 1 + 1j, 1j, 1j - 1, -1]

prev = set(elves)
solution_2 = 0

while True:

    once = set()
    twice = set()

    for elf in elves:
        if all(elf + x not in elves for x in offsets): continue

        for move in moves:
            if all(elf + x not in elves for x in scan_map[move]):
                prop = elf + move

                if prop in twice:
                    pass 
                elif prop in once:
                    twice.add(prop)
                else:
                    once.add(prop)
                break

    elves_clone = set(elves)

    for elf in elves_clone:
        if all(elf + x not in elves_clone for x in offsets): continue

        for move in moves:
            if all(elf + x not in elves_clone for x in scan_map[move]):
                prop = elf + move
                
                if prop not in twice:
                    elves.remove(elf)
                    elves.add(prop)

                break

    moves.append(moves.pop(0))

    solution_2 += 1
    if prev == elves:
        break

    prev = set(elves)

    if solution_2 == 10:
        minx = int(min(x.real for x in elves))
        miny = int(min(x.imag for x in elves))
        maxx = int(max(x.real for x in elves))
        maxy = int(max(x.imag for x in elves))

        total_area = (maxx - minx + 1) * (maxy - miny + 1)
        solution_1 = total_area - len(elves)


print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")
