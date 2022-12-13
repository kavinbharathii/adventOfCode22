
# --------------------------------------------------------- parse input --------------------------------------------------------- #

with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()


def valid(left, right):

    # If the left and right values are integers, compare them
    if type(left) == int and type(right) == int:
        if left < right:
            return 1

        elif left > right:
            return 0
        
        # If they are equal, we have to check the next element
        else:
            return -1

    else:
        # If both left and right are lists
        if type(left) == list and type(right) == list:
            ind = 0
            # Check until one is fully traversed
            while ind < len(left) and ind < len(right):
                res = valid(left[ind], right[ind])
                if res == 1:
                    return 1
                elif res == 0:
                    return 0
                else:
                    ind += 1

            # If left is shorter, True
            if ind == len(left) and ind < len(right):
                return 1

            # If right is shorter return False
            elif ind == len(right) and ind < len(left):
                return 0

            # Else, go to the next element
            else:
                return -1

        # If only one of them is a list, convert the other to a list too.
        elif type(left) == list:
            return valid(left, [right])
        else:
            return valid([left], right)

# ----------------------------------------------------------- part 1 ------------------------------------------------------------ #

data = [[]]

for i in raw_data:
    if i == '':
        data.append([])
    else:
        data[-1].append(eval(i))

solution_1 = 0

for ind, [l, r] in enumerate(data):
    res = valid(l, r)
    if res == 1:
        solution_1 += ind + 1

# ----------------------------------------------------------- part 2 ------------------------------------------------------------ #

data = []

for i in raw_data:
    if i == '':
        pass
    else:
        data.append([eval(i), 0])

# markers
data.append([[[2]], 0])      # marker 1
data.append([[[6]], 0])      # marker 2    

for ind, [d1, val1] in enumerate(data):
    for d2, val2 in data:
        if d1 != d2:
            if valid(d1, d2):
                data[ind][-1] += 1


data.sort(key = lambda x : x[-1])
data.reverse()

solution_2 = 1

for ind, [d, val] in enumerate(data):
    if d == [[2]] or d == [[6]]:
        solution_2 *= ind + 1

# ----------------------------------------------------------------------------------------------------------------------------- #

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

# ----------------------------------------------------------------------------------------------------------------------------- #
