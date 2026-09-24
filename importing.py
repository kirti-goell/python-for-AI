# pattern 1 : importing the whole module
import math
math.sqrt(16)

# pattern 2 : importing specific items from module
from math import sqrt , pi
sqrt(16)


import random
number = random.randint(1,10)
number
# every time it will return diff value

choice = random.choice(["apple","mango","banana"])
choice

import datetime
today = datetime.date.today()
print(today)

import os
current = os.getcwd()
print(current)

import json
data = {"name": "kirti", "age": 23}
json_string = json.dumps(data)
print(json_string)


# import with alias
import pandas as pd
df = pd.DataFrame(data)
print(df)

# importing evrything (avoid this)
from math import *