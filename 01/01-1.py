instructions = open('input').read()

x = 0
y = 0

direction = 0

for instruction in instructions.strip().split(", "):
    if instruction[0] == "R":
        direction += 1
    if instruction[0] == "L":
        direction -= 1

    direction = direction % 4
    distance = int(instruction[1:])

    if direction == 0:
        y += distance
    if direction == 1:
        x += distance
    if direction == 2:
        y -= distance
    if direction == 3:
        x -= distance

print "Grid Distance " + str(abs(x) + abs(y))
