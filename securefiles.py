"""
securefiles:

Its a weird name for this program, but we named it that so.. yea.

This program was created to ensure that files wouldn't get corrupted or
get overwritten during the conversion process.

So, this essentially... secures your files!

"""


import random
import string

def randomstring(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
