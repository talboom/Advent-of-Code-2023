from utils import read_input
import time
from collections import defaultdict

input = read_input("day17.txt")
nodes = [list(int(x) for x in line) for line in input]

directions = [(-1,0),(0,1),(1,0),(0,-1)]

# part 1

# cost, pos, direction, num_steps
paths = defaultdict(list)
paths[0].append([(0,0), 1, 0])
paths[0].append([(0,0), 2, 0])

target = (len(nodes)-1, len(nodes[0])-1)
h, w = target
visted = set()


start_time = time.time()

c = 0 

while paths:
    while not paths[c]:
        c += 1

    path = paths[c].pop(0)        

    if path[0] == target:
        print(c)
        break

    if (path[0], path[1], path[2]) in visted:
        continue
    visted.add((path[0], path[1], path[2]))

    l = (path[0][0] + directions[(path[1] - 1) % 4][0], path[0][1] + directions[(path[1] - 1) % 4][1])
    r = (path[0][0] + directions[(path[1] + 1) % 4][0], path[0][1] + directions[(path[1] + 1) % 4][1])
    f = (path[0][0] + directions[path[1]][0], path[0][1] + directions[path[1]][1])


    if 0 <= l[0] <= h and 0 <= l[1] <= w:
        paths[c+nodes[l[0]][l[1]]].append([ l, (path[1]-1)%4, 1]) 
    if 0 <= r[0] <= h and 0 <= r[1] <= w:
        paths[c+nodes[r[0]][r[1]]].append([r, (path[1]+1)%4, 1]) 
    if 0 <= f[0] <= h and 0 <= f[1] <= w and path[2] < 3:
        paths[c+nodes[f[0]][f[1]]].append([f, path[1], path[2]+1]) 

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")


# part 2

# cost, pos, direction, num_steps
paths = defaultdict(list)
paths[0].append([(0,0), 1, 0])
paths[0].append([(0,0), 2, 0])

target = (len(nodes)-1, len(nodes[0])-1)
h, w = target
visted = set()


start_time = time.time()

c = 0 

while paths:
    while not paths[c]:
        c += 1

    path = paths[c].pop(0)        

    if path[0] == target and path[2] >= 4:
        print(c)
        break

    if (path[0], path[1], path[2]) in visted:
        continue
    visted.add((path[0], path[1], path[2]))

    l = (path[0][0] + directions[(path[1] - 1) % 4][0], path[0][1] + directions[(path[1] - 1) % 4][1])
    r = (path[0][0] + directions[(path[1] + 1) % 4][0], path[0][1] + directions[(path[1] + 1) % 4][1])
    f = (path[0][0] + directions[path[1]][0], path[0][1] + directions[path[1]][1])


    if 0 <= l[0] <= h and 0 <= l[1] <= w and path[2] >= 4:
        paths[c+nodes[l[0]][l[1]]].append([ l, (path[1]-1)%4, 1]) 
    if 0 <= r[0] <= h and 0 <= r[1] <= w and path[2] >= 4:
        paths[c+nodes[r[0]][r[1]]].append([r, (path[1]+1)%4, 1]) 
    if 0 <= f[0] <= h and 0 <= f[1] <= w and path[2] < 10:
        paths[c+nodes[f[0]][f[1]]].append([f, path[1], path[2]+1]) 

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")

