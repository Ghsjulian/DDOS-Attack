import sys
import os 
import random 
import color

"""

def save_data(data):
    f = open("matrix.txt", "w")
    f.write(data)
    f.close()

byte = str(random._urandom(1490)*30)
mystr = ""

for char in byte:
    rnd_col = random.choice(color.color_list)
    mystr += rnd_col+str(char)+"        &"
save_data(mystr)

"""

with open("matrix.txt") as matrix:
    data = matrix.read()
    print(data)
    print(data)
