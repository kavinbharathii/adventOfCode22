
with open("data.aoc", "r") as file:
    gas = [1 if i == '>' else -1 for i in file.readline()]
    file.close()

# [CERTIFIED MINDBLOWN MOMENT RIGHT HERE]
rocks = [
    [0, 1, 2, 3],
    [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
    [0, 1, 2, 2 + 1j, 2 + 2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1 + 1j]
]

solid = {x - 1j for x in range(7)}
height = 0 

rock_count = 0
rock_index = 0
rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}

# while rock_count < 2022:
#     for jet in gas:
#         moved = {x + jet for x in rock}
#         if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
#             rock = moved
#         moved = {x - 1j for x in rock}
#         if moved & solid:
#             solid |= rock
#             rock_count += 1
#             height = max(x.imag for x in solid) + 1

#             if rock_count >= 2022:
#                 break

#             rock_index = (rock_index + 1) % 5
#             rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}

#         else:
#             rock = moved

# print(int(height))


trillo = 1_000_000_000_000
seen = {}

def detect():
    lookups = [-20] * 7

    for seg in solid:
        r = int(seg.real)
        i = int(seg.imag)
        lookups[r] = max(lookups[r], i)

    
    top = max(lookups)
    return tuple(x - top for x in lookups)


while rock_count < trillo:
    for jet_index, jet in enumerate(gas):
        moved = {x + jet for x in rock}
        if all(0 <= x.real < 7 for x in moved) and not (moved & solid):
            rock = moved
        moved = {x - 1j for x in rock}
        if moved & solid:
            solid |= rock
            rock_count += 1
            height = max(x.imag for x in solid) + 1

            if rock_count >= trillo:
                break

            rock_index = (rock_index + 1) % 5
            rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]}
            key = (jet_index, rock_index, detect())

            if key in seen:
                prev_rock_count, prev_height = seen[key]
                rem = trillo - rock_count 
                rep = rem // (rock_count - prev_rock_count)
                offset = rep * (height - prev_height)
                rock_count += rep * (rock_count - prev_rock_count)
                seen = {}

            seen[key] = (rock_count, height)

        else:
            rock = moved

print(int(height + offset))
