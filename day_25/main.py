
# Advent Of Code => day 25 
# ----------------------------------------------------------------------------------------------------------------------------- #
import sys

file_name = sys.argv[1] if len(sys.argv) > 1 else "data.aoc"

with open(file_name, "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()
    
int_to_snafu = {
    -2 : "=",
    -1 : '-',
     0 : '0',
     1 : '1',
     2 : '2'
}

# ----------------------------------------------------------------------------------------------------------------------------- #

def from_snafu(num):
    degree = len(num) - 1
    dec_num = 0

    for char in num:
        match char:
            case '2' | '1' | '0':
                place_value = int(char)            
            case '-':
                place_value = -1
            case '=':
                place_value = -2
            case _:
                # No way, but if it happens...
                assert False, char
    
        dec_num += place_value * pow(5, degree)
        degree -= 1

    return dec_num

# ----------------------------------------------------------------------------------------------------------------------------- #

# Transform a given number to SNAFU representation
def to_snafu(num):
    res = []
    while num > 0:
        rem = ((num + 2) % 5) - 2
        res.append(int_to_snafu[rem])
        num -= rem
        num //= 5

    return ''.join(list(reversed(res)))

# ----------------------------------------------------------------------------------------------------------------------------- #

total = 0

for data in raw_data:
    total += from_snafu(data)

print(total)
print(to_snafu(total))

# ----------------------------------------------------------------------------------------------------------------------------- #
