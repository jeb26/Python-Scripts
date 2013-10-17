import random

def generate(numRandoms):
    for i in range(numRandoms):
        num = random.randint(0,64000)
        print hex(num),

generate(10)
