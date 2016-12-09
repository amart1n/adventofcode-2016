instructions = open('input').read()

code = ""

x = -2
y = 0

for instruction in instructions.split("\n"):

    if len(instruction) > 0:

        for i in range(len(instruction)):

            if instruction[i] == "R":
                x = min(x + 1, (4 - (abs(y) * 2)) / 2)
            if instruction[i] == "L":
                x = max(x - 1, -1 * (4 - (abs(y) * 2)) / 2)
            if instruction[i] == "U":
                y = max(y - 1, -1 * (4 - (abs(x) * 2)) / 2)
            if instruction[i] == "D":
                y = min(y + 1, (4 - (abs(x) * 2)) / 2)

        code += hex(7 + (y * 4) + x)[2:].upper()

print "Code: " + code
