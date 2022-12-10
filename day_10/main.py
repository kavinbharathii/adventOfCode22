
# ---------------------------------------------------- parse input ---------------------------------------------------- #

with open("data.txt", "r") as file:
    cmds = [line.strip() for line in file.readlines()]
    file.close()

# ------------------------------------------------------ part one ------------------------------------------------------ #

solution_1 = 0
register = 1
cycle = 0

check_cycle = 20

# Since "addx" commands are 2 cycles out of which only one, we add the value V
# we can interpret "addx" commands as 1 "noop" and one "addx" command, each with
# a single cycle. So to do that, we extend each "addx" as "noop" + "addx"
new_cmds = []
for cmd in cmds:
    if cmd == "noop":
        new_cmds.append(cmd)
    else:
        new_cmds.append("noop")
        new_cmds.append(cmd)

cmds = new_cmds

for cmd in cmds:
    if cmd == "noop":
        cycle += 1

        # if the cycle corresponds to the cycle we need to check,
        # record the values and increment by 40
        if cycle == check_cycle:
            solution_1 += register * cycle
            check_cycle += 40
        
    else:
        cmd = cmd.split()
        V = int(cmd[-1])

        cycle += 1

        if cycle == check_cycle:
            solution_1 += register * cycle
            check_cycle += 40
        
        # add the value at the end of the cycle
        register += V

# ------------------------------------------------------ part two ------------------------------------------------------ #

register = 1
cycle = 0
sprite = 0

# Each row of the CRT screen is represented by crt variable
crt = ''
crts = []

for index, cmd in enumerate(cmds):
    if cmd == "noop":
        cycle += 1

        if sprite <= index <= sprite + 2:
            crt += '#'
        else:
            crt += ' '                    # changing the '.', given in question to ' ', for the sake of convenience

        # If the "crt" reaches 40 chars, save the current state,
        # and reset the state of "crt" to ''.
        if len(crt) == 40:
            crts.append(crt)
            crt = ''
            sprite += 40

    else:
        cmd = cmd.split()
        V = int(cmd[-1])

        cycle += 1

        if sprite <= index <= sprite + 2:
            crt += '#'
        else:
            crt += ' '
        
        if len(crt) == 40:
            crts.append(crt)
            crt = ''
            sprite += 40


        # Since the value of the sprite is added at the end of each cycle, 
        # we have to add in after everything (cycle, crt ...) to update before 
        # we update the sprite value.
        sprite += V

# ---------------------------------------------------------------------------------------------------------------------- #

# Part 1 solution:
print(f"Part 1: {solution_1}")

# Part 2 solution:
print("\nPart 2: ")

# Display the full CRT screen, which displays a 8 letter word
for row in crts:
    print(row)

