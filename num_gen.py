import random
import time
def generate(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,9999))
    return arr
