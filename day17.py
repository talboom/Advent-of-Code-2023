from utils import read_input

input = read_input("day17_test.txt")
grid = [c for s in input for c in s]

h,w = len(grid), len(grid[0])
grid_loss = [[0]*w for _ in range(h)]

pos = (0,0)
direction = (0,1)

for i, line in enumerate(grid):
    for j,p in enumerate(line):
        for x in range(i):
            for y in range(j):
                grid_loss[x][y] =

2 4
3 2
    
0 4
3 5

2 4 1
3 2 1
3 2 5
    
0 4 5
3 5 6
6 7 11