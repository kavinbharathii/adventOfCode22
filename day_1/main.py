
# Maximum calories

with open("data.txt", "r") as file:
    raw_data = file.readlines()
    file.close()

maximum_calories = 0
calories_per_elf = 0
calorie_data = []
for line in raw_data:
    if line == '\n':
        if calories_per_elf > maximum_calories:
            maximum_calories = calories_per_elf
        calorie_data.append(calories_per_elf)
        calories_per_elf = 0
    else:
        calories_per_elf += int(line.strip())

calorie_data.sort()
calorie_data.reverse()

top_three_calorie_sum = sum(calorie_data[:3])


print(f"Part 1: {maximum_calories}")
print(f"Part 2: {top_three_calorie_sum}")
