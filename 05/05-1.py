import hashlib
import re

door = "ffykfhsq"

password = ""
i = 0

while len(password) < 8:

    md5 = hashlib.md5()
    md5.update(door + str(i))

    if re.match(r"^00000", md5.hexdigest()):
        password += md5.hexdigest()[5]

    i += 1

print password
