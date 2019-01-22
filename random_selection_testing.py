from random import *

data = range(10000)

import whrandom

def select(data):
    if data != []:
        index = whrandom.randint(0, len(data) - 1)
        elem = data[index]
        data[index] = data[-1]
        del data[-1]
        return elem
    else:
        return data

print select(data)