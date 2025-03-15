import random
def generate(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,999999))
    return arr
