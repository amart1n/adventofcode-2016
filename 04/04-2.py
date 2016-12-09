import re

sectors = open('input').read()
total = 0

for sector in sectors.split("\n"):

    if not sector:
        continue

    letters = dict()
    sector_id = re.search(r"\d+", sector).group(0)
    checksum = re.search(r"\[(.*?)\]", sector).group(1)
    full_code = re.match(r"[a-z-]+", sector).group(0)
    codes = full_code.replace("-", "")

    for code in codes:
        if not code in letters:
            letters[code] = 1
        else:
            letters[code] += 1

    letters = [value[0] for value in sorted(letters.iteritems(), key=lambda(key, value): (-value, key))]

    wrong = False

    for i in range(len(checksum)):
        if checksum[i] != letters[i]:
            wrong = True
            break

    if wrong == False:
        name = ""
        for i in range(len(full_code)):
            if full_code[i] == "-":
                name += " "
                continue

            ascii_code = (ord(full_code[i]) - 97 + int(sector_id)) % 26
            name += chr(ascii_code + 97)

        print "Name: " + name + " [" + str(sector_id) + "]"
