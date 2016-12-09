instructions = open('input').read()

x = 0
y = 0

direction = 0

locations = ["0,0"]

for instruction in instructions.strip().split(", "):
    if instruction[0] == "R":
        direction += 1
    if instruction[0] == "L":
        direction -= 1

    direction = direction % 4
    distance = int(instruction[1:])

    for i in range(0, distance):

        if direction == 0:
            y += 1
        if direction == 1:
            x += 1
        if direction == 2:
            y -= 1
        if direction == 3:
            x -= 1


        coords = (str(x) + "," + str(y))

        if coords in locations:
            print "Grid Distance " + str(abs(x) + abs(y))
            exit()

        locations.append(coords)
