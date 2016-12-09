instructions = open('input').read()

code = ""

x = 2
y = 2

for instruction in instructions.split("\n"):

    if len(instruction) > 0:

        for i in range(len(instruction)):

            if instruction[i] == "R":
                x = min(x + 1, 3)
            if instruction[i] == "L":
                x = max(x - 1, 1)
            if instruction[i] == "U":
                y = max(y - 1, 1)
            if instruction[i] == "D":
                y = min(y + 1, 3)

        code += str(x + (3 * y) - 3)

print "Code: " + code
