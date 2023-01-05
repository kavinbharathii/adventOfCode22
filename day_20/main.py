
with open("data.aoc", "r") as file:
    raw_data = [int(line.strip()) for line in file.readlines()]  
    file.close()

orig = raw_data[:]
data = list(enumerate(raw_data))
curr = 0

def get(ind):
    for r_index, value in enumerate(data):
        if value[0] == ind: return r_index
    return None

def get_by_element(ele):
    for r_index, value in enumerate(data):
        if value[1] == ele: return r_index
    return None

def print_data(curr, data):
    print(curr, end=": ")
    print(" ".join(str(i[1]) for i in data))

# [part 1]
while curr < len(orig):
    # print_data(curr, data)
    ri = get(curr) 
    temp = data[:]
    ele = temp.pop(ri)
    togo = (ri + ele[1]) % len(temp)

    if temp[:togo] != []:
        new_temp = temp[:togo] + [ele] + temp[togo:]
    else:
        new_temp = temp[togo:] + [ele]

    data = new_temp[:]
    
    curr += 1


ind_0 = get_by_element(0)
th_1000 = data[(ind_0 + 1000) % len(orig)][1]
th_2000 = data[(ind_0 + 2000) % len(orig)][1]
th_3000 = data[(ind_0 + 3000) % len(orig)][1]

solution_1 = th_1000 + th_2000 + th_3000


# [part 2]
decrypt_key = 811589153
data = [decrypt_key * val for val in raw_data]
data = list(enumerate(data))
curr = 0

for _ in range(10):
    while curr < len(orig):
        ri = get(curr) 
        temp = data[:]
        ele = temp.pop(ri)
        togo = (ri + ele[1]) % len(temp)

        if temp[:togo] != []:
            new_temp = temp[:togo] + [ele] + temp[togo:]
        else:
            new_temp = temp[togo:] + [ele]

        data = new_temp[:]
        
        curr += 1

    curr = 0

ind_0 = get_by_element(0)
th_1000 = data[(ind_0 + 1000) % len(orig)][1]
th_2000 = data[(ind_0 + 2000) % len(orig)][1]
th_3000 = data[(ind_0 + 3000) % len(orig)][1]

solution_2 = th_1000 + th_2000 + th_3000

print(f"Part 1: {solution_1}")
print(f"Part 2: {solution_2}")

