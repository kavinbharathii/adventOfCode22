
with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

alphas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total_score = 0

for data in raw_data:
    mid = len(data) // 2
    left, right = data[:mid], data[mid:]
    for letter in left:
        if letter in right:
            total_score += alphas.index(letter) + 1
            break

solution_1 = total_score
total_score = 0

raw_data = [[raw_data[i * 3], raw_data[i * 3 + 1], raw_data[i * 3 + 2]] for i in range(len(raw_data) // 3)]

for data in raw_data:
    a, b, c = data
    for letter in a:
        if letter in b and letter in c:
            total_score += alphas.index(letter) + 1
            break

solution_2 = total_score
print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")
