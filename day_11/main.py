
import math
from copy import deepcopy

# ---------------------------------------------------- parse input ---------------------------------------------------- #

with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()


class Monkey:
    def __init__(self, ind, stuff = None, op = None, condition = None, true_monkey = None, false_monkey = None, lcm_ = None):
        self.ind = ind
        self.stuff = stuff
        self.op = op
        self.condition = condition
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect_count = 0
        self.lcm_ = lcm_

    def inspect(self):
        if self.stuff != []:
            rem_ind = []
            for index, stuff in enumerate(self.stuff):
                stuff = eval(self.op.replace("old", str(stuff)))        # perform the monkey's operation and evaluate the operation result
                if self.lcm_ != None:
                    stuff = stuff % self.lcm_                           # lcm check for part 2
                else:
                    stuff = stuff // 3                                  # "bored" operation

                # passing the object to the respective monkeys
                if stuff % self.condition == 0:
                    self.true_monkey.stuff.append(stuff)
                else:
                    self.false_monkey.stuff.append(stuff)

                rem_ind.append(index)
                self.inspect_count += 1

            # removing object from monkey
            self.stuff = [self.stuff[i] for i in range(len(self.stuff)) if i not in rem_ind]

    def __str__(self) -> str:
        return f"Monkey {self.ind}: {' '.join([str(i) for i in self.stuff])}"


monkeys = dict()

curr = -1
for line in raw_data:
    check = line.strip().split()
    if line != '':
        if check[0] == "Monkey":
            curr = int(check[-1].strip(':')) 
            monkeys[curr] = dict()

        elif check[0] == "Starting":
            stuff = line.split(":")[-1].strip().split(', ')
            stuff = [int(i) for i in stuff]
            # print(stuff)
            monkeys[curr]["Stuff"] = stuff
        
        elif check[0] == "Operation:":
            op = line.split('=')[-1].strip()
            # print(op)
            monkeys[curr]["Operation"] = op
        
        elif check[0] == "Test:":
            condition = int(line.split()[-1])
            # print(condition)
            monkeys[curr]["Condition"] = condition

        elif check[0] == "If":
            if check[1] == "true:":
                true_monkey = int(line.split()[-1])
                # print(true_monkey)
                monkeys[curr]["True"] = true_monkey

            elif check[1] == "false:":
                false_monkey = int(line.split()[-1])
                # print(false_monkey)
                monkeys[curr]["False"] = false_monkey

new_monkeys = deepcopy(monkeys)

# ------------------------------------------------------ part one ------------------------------------------------------ #

monks = [Monkey(i) for i in range(len(monkeys.keys()))]

for monk, val in monkeys.items():
    monks[monk].stuff = val["Stuff"]
    monks[monk].op = val["Operation"]
    monks[monk].condition = val["Condition"]
    monks[monk].true_monkey = monks[val["True"]]
    monks[monk].false_monkey = monks[val["False"]]

for _ in range(20):
    for monk in monks:
        monk.inspect()

inspects = [m.inspect_count for m in monks]
inspects.sort()
inspects.reverse()

solution_1 = inspects[0] * inspects[1]


for monk in monks:
    del monk

del monks

# ------------------------------------------------------ part two ------------------------------------------------------ #

lcm_ = 1

for _, val in monkeys.items():
    lcm_ = math.lcm(lcm_, val["Condition"])

monks = [Monkey(i) for i in range(len(monkeys.keys()))]

for monk, val in new_monkeys.items():
    monks[monk].stuff = val["Stuff"]
    monks[monk].op = val["Operation"]
    monks[monk].condition = val["Condition"]
    monks[monk].true_monkey = monks[val["True"]]
    monks[monk].false_monkey = monks[val["False"]]
    monks[monk].lcm_ = lcm_

    # reset the inspect count
    monks[monk].inspect_count = 0

for _ in range(10000):
    for monk in monks:
        monk.inspect()

inspects = [m.inspect_count for m in monks]
inspects.sort()
inspects.reverse()

solution_2 = inspects[0] * inspects[1]

# ---------------------------------------------------------------------------------------------------------------------- #

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# ---------------------------------------------------------------------------------------------------------------------- #

