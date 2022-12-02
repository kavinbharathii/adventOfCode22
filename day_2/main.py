
# Rock      : A X  
# Paper     : B Y
# Scissor   : C Z

shape_score = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

win_conditions = {
    "X" : "C",
    "Y" : "A",
    "Z" : "B",
}

lose_conditions = {
    "X" : "B",
    "Y" : "C",
    "Z" : "A",
}

with open("data.txt", "r") as file:
    raw_data = file.readlines()
    file.close()

total_score = 0

# --------------------------- part 1 --------------------------- #

for line in raw_data:
    opponent, yourself = line.strip().split(" ")
    total_score += shape_score[yourself]
    if win_conditions[yourself] == opponent:
        total_score += 6
    elif lose_conditions[yourself] == opponent:
        total_score += 0
    else:
        total_score += 3

solution_one = total_score
# -------------------------------------------------------------- #


outcome_score = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

win_conditions = {
    "A" : "Y",
    "B" : "Z",
    "C" : "X",
}

lose_conditions = {
    "A" : "Z",
    "B" : "X",
    "C" : "Y",
}

notation_change = {
    "A" : "X",  
    "B" : "Y",
    "C" : "Z",
}

total_score = 0

# --------------------------- part 2 --------------------------- #
for line in raw_data:
    opponent, outcome = line.strip().split(" ")
    total_score += outcome_score[outcome]

    if outcome == "X":
        total_score += shape_score[lose_conditions[opponent]]
    if outcome == "Y":
        total_score += shape_score[notation_change[opponent]]
    if outcome == "Z":
        total_score += shape_score[win_conditions[opponent]]

solution_two = total_score
# -------------------------------------------------------------- #

print(f"Part 1: {solution_one}")
print(f"Part 2: {solution_two}")
