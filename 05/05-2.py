import hashlib
import re

door = "ffykfhsq"

password = {}
i = 0

while len(password) < 8:

    md5 = hashlib.md5()
    md5.update(door + str(i))

    if re.match(r"^00000", md5.hexdigest()) and int(md5.hexdigest()[5], 16) < 8:
        if not int(md5.hexdigest()[5]) in password:
            password[int(md5.hexdigest()[5])] = md5.hexdigest()[6]

    i += 1

print "".join(str(x) for x in password.values())
