import re

triangles = open('input').read()

count = 0

for triangle in triangles.split("\n"):
    if triangle:
        sides = map(int, re.findall(r"(\d+)", triangle))
    else:
        continue

    if (sides[0] + sides[1]) <= sides[2]:
        continue
    if (sides[1] + sides[2]) <= sides[0]:
        continue
    if (sides[0] + sides[2]) <= sides[1]:
        continue

    count += 1

print "Count: " + str(count)
