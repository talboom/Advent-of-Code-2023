from utils import read_input
from collections import defaultdict

input = read_input("day15.txt")
sequence = input[0].split(',')
test = "HASH"

def get_number(string):
    value = 0
    for c in string:
        v = ord(c)
        value = 17*(value+v) % 256
    return value

part_1 = 0
for s in sequence:
    part_1 += get_number(s)
print(part_1)

# Part 2
boxes = dict()
for s in sequence:
    if "-" in s:
        s = s.split('-')
        v = get_number(s[0])
        if v in boxes and s[0] in boxes[v]:
            del boxes[v][s[0]]
    if "=" in s:
        s = s.split('=')
        v = get_number(s[0])
        if v in boxes:
            boxes[v][s[0]] = int(s[1])
        else:
            boxes[v] = dict()
            boxes[v][s[0]] = int(s[1])
part_2 = 0
for b in boxes:
    for i,l in enumerate(boxes[b]):
        part_2 += (int(b)+1) * (i+1) * boxes[b][l]
print(part_2)