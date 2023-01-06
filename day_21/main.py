
import sympy

with open("data.aoc", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]  
    file.close()

monkeys = {"humn" : sympy.Symbol("x")}

ops = {
    "+" : lambda x, y: x + y,
    "-" : lambda x, y: x - y,
    "*" : lambda x, y: x * y,
    "/" : lambda x, y: x / y,
}

for line in raw_data:
    name, expr = line.split(": ")

    if name in monkeys: continue

    if expr.isdigit():
        monkeys[name] = sympy.Integer(expr)

    else:
        left, op, right = expr.split()
        if left in monkeys and right in monkeys:
            if name == "root":
                print(sympy.solve(monkeys[left] - monkeys[right])[0])
                break

            monkeys[name] = ops[op](monkeys[left], monkeys[right])

        else:
            raw_data.append(line)

