
from math import ceil

with open("data.aoc", "r") as file:
    raw_data = [line.strip().strip('.') for line in file.readlines()]  
    file.close()

materials = ["ore", "clay", "obsidian"]


def dfs(bp, max_spend, cache, time, bots, amt):
    if time == 0:
        return amt[3]

    key = tuple([time, *bots, *amt])
    if key in cache:
        return cache[key]

    max_val = amt[3] + bots[3] * time

    for bot_type, recipe in enumerate(bp):
        if bot_type != 3 and bots[bot_type] >= max_spend[bot_type]:
            continue

        wait = 0
        for ramt, rtype in recipe:
            if bots[rtype] == 0:
                break
            wait = max(wait, ceil((ramt - amt[rtype]) / bots[rtype]))
        else:
            remtime = time - wait - 1
            if remtime <= 0:
                continue
            bots_ = bots[:]
            amt_ = [x + y * (wait + 1) for x, y in zip(amt, bots)]
            for ramt, rtype in recipe:
                amt_[rtype] -= ramt
            bots_[bot_type] += 1
            for i in range(3):
                amt_[i] = min(amt_[i], max_spend[i] * remtime)
            max_val = max(max_val, dfs(bp, max_spend, cache, remtime, bots_, amt_))

    cache[key] = max_val
    return max_val 


# total = 0

# for line in raw_data:
#     blue_print_id = int(line.split()[1].strip(':'))
#     max_spend = [0, 0, 0]
#     blue_print = []
    
#     for section in line.split(': ')[1].split('.'):
#         recipe = []
#         section = section.split()
#         for index, token in enumerate(section):
#             if token.isnumeric():
#                 token = int(token)
#                 material = materials.index(section[index + 1])

#                 max_spend[material] = max(max_spend[material], token)
#                 recipe.append((int(token), materials.index(section[index + 1])))

#         blue_print.append(recipe)
    
#     geodes = dfs(blue_print, max_spend, {}, 28, [1, 0, 0, 0], [0, 0, 0, 0])
#     total += blue_print_id * geodes

# print(total)


solution_2 = 1

data_p2 = raw_data[:3]

for line in data_p2:
    blue_print_id = int(line.split()[1].strip(':'))
    max_spend = [0, 0, 0]
    blue_print = []
    
    for section in line.split(': ')[1].split('.'):
        recipe = []
        section = section.split()
        for index, token in enumerate(section):
            if token.isnumeric():
                token = int(token)
                material = materials.index(section[index + 1])

                max_spend[material] = max(max_spend[material], token)
                recipe.append((int(token), materials.index(section[index + 1])))

        blue_print.append(recipe)
    
    geodes = dfs(blue_print, max_spend, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
    solution_2 *= geodes

print(solution_2)
