import re

triangles = open('input').read()

count = 0
batch_count = 1
batches = []

for triangle in triangles.split("\n"):
    if triangle:
        batches.append(map(int, re.findall(r"(\d+)", triangle)))
    else:
        continue

    batch_count += 1

    if (batch_count - 1) % 3 == 0:

        for i in range(0, 3):

            if (batches[0][i] + batches[1][i]) <= batches[2][i]:
                continue
            if (batches[1][i] + batches[2][i]) <= batches[0][i]:
                continue
            if (batches[0][i] + batches[2][i]) <= batches[1][i]:
                continue

            count += 1
        batches = []

print "Count: " + str(count)
