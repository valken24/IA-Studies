#own modules
#thirdy party modules
#python modules

import datetime

print(datetime.timedelta(minutes=70))

from datetime import timedelta

print(timedelta(minutes=100))


import fmath
from fmath import add, subs

fmath.add(50,30)
fmath.subs(50,30)

add(50,30)
subs(50,30)

from colorama import Fore, Style, init
init(convert=True)
print(Fore.RED+"Hello World")



