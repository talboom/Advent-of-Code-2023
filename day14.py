from utils import read_input

input = read_input("day14.txt")

cols = [[]  for _ in range(len(input[0]))]

for i, line in enumerate(input):
    for j, char in enumerate(line):
        if char == "O":
            cols[j].append(char)
        if char == "#":
            if (fill := i-len(cols[j])) > 0:
                cols[j] += ["."]*(fill)
            cols[j].append(char)

part_1 = 0
for i, col in enumerate(cols):
    if len(col) < len(input):
                col += ["."]*(len(input)-len(col))
    for j, char in enumerate(reversed(col)):
        if char == "O":
            part_1 += j+1

print(part_1)

# PART 2
field = input
def tilt(field):
    cols = [[]  for _ in range(len(input[0]))]

    for i, line in enumerate(field):
        for j, char in enumerate(line):
            if char == "O":
                cols[j].append(char[0])
            if char == "#":
                if (fill := i-len(cols[j])) > 0:
                    cols[j] += "."*(fill)
                cols[j].append(char[0])
    new_cols = []
    for i, col in enumerate(cols):
        if len(col) < len(field):
                    cols[i] += ["."]*(len(input)-len(col))
        new_cols.append(col[::-1])
    return new_cols

rocks = set()
cubes = set()
h,w = len(field), len(field[0])
for i, line in enumerate(input):
    for j,p in enumerate(line):
        if p == "O":
            rocks.add((i, j))
        if p == "#":
            cubes.add((i, j))
rocks = tuple(rocks)

def tilt(h,w,rocks,cubes,direction):
    new_rocks = set()
    for rock in sorted(rocks, key=lambda r: sum(-x * y for x, y in zip(r, direction))):
        new_rock = rock
        while new_rock[0] >= 0 and new_rock[0] < w and new_rock[1] >= 0 and new_rock[1] < h and new_rock not in cubes and new_rock not in new_rocks:
             rock = new_rock
             new_rock = tuple(r + d for r, d in zip(rock, direction))
        new_rocks.add(rock)
        
    return tuple(sorted(new_rocks))

rotations = [(-1,0),(0,-1),(1,0),(0,1)]
sets_list = []
sets = set()
i = 0
while rocks not in sets:
    i += 1
    sets.add(rocks)
    sets_list.append(rocks)
    for r in rotations:
        rocks = tilt(h,w,rocks,cubes,r)
    
index = sets_list.index(rocks)
set_index = (1000000000 - index) % (i - index) + index
rock_config = sets_list[set_index]

part_2 = sum(h-x[0] for x in rock_config)

print(part_2)
