from utils import read_input

input = read_input("day10.txt")

symbol_pipe = {
  '|' : [1,0,1,0],
  '-' : [0,1,0,1],
  'L' : [1,1,0,0],
  'J' : [1,0,0,1],
  '7' : [0,0,1,1],
  'F' : [0,1,1,0]}

# find start position
for i, line in enumerate(input):
  if (line.find('S')) > -1:
    start_position = [i, line.find('S')]
    break
position = start_position

# create twin
twin = [['.']*len(line) for line in input]


# get start symbol
north = input[start_position[0]-1][start_position[1]]
east = input[start_position[0]][start_position[1]+1]
south = input[start_position[0]+1][start_position[1]]

if north in ['|','7','F'] and start_position[0] > 0:
  start_symbol = north
  start_direction = [1,0,0,0]
elif east in ['-','7','J'] and start_position[1] < len(input[0])-1:
  start_symbol = east
  start_direction = [0,1,0,0]
elif south in ['|','J','L'] and start_position[0] < len(input)-1:
  start_symbol = south
  start_direction = [0,0,1,0]

# PART 1
symbol = start_symbol
direction = start_direction
position = [position[0]-direction[0]+direction[2], position[1]+direction[1]-direction[3]]
twin[position[0]][position[1]] = symbol
steps = 0
while symbol != 'S':
  direction_orig = direction[2:] + direction[:2]
  direction = [x - y for x, y in zip(symbol_pipe[symbol], direction_orig)]
  position = [position[0]-direction[0]+direction[2], position[1]+direction[1]-direction[3]]
  symbol = input[position[0]][position[1]]
  twin[position[0]][position[1]] = symbol
  steps += 1
print((steps+1)/2)

# PART 2
position = start_position
symbol = start_symbol
direction = start_direction
position = [position[0]-direction[0]+direction[2], position[1]+direction[1]-direction[3]]
while symbol != 'S':
  #find next step direction
  direction_orig = direction[2:] + direction[:2]
  direction = [x - y for x, y in zip(symbol_pipe[symbol], direction_orig)]
  
  # if neightor with 0 is a . make I or O
  j = direction_orig.index(1)
  outside_direction = [0,0,0,0]
  
  # determine if outside
  for i in range(4):
    if direction [(j+i)%4] == 1:
      break
    else:  
      outside_direction[(j+i)%4] = 1

  # fill in outside
  if outside_direction[0] == 1 and position[0] > 0 and twin[position[0]-1][position[1]] == '.':
    twin[position[0]-1][position[1]] = 'O'
  if outside_direction[1] == 1 and position[1] < len(input[0])-1 and twin[position[0]][position[1]+1] == '.':
    twin[position[0]][position[1]+1] = 'O'
  if outside_direction[2] == 1 and position[0] < len(input)-1 and twin[position[0]+1][position[1]] == '.':
    twin[position[0]+1][position[1]] = 'O'
  if outside_direction[3] == 1 and position[1] > 0 and twin[position[0]][position[1]-1] == '.':
    twin[position[0]][position[1]-1] = 'O'
  
  direction = [x - y for x, y in zip(symbol_pipe[symbol], direction_orig)]
  position = [position[0]-direction[0]+direction[2], position[1]+direction[1]-direction[3]]
  symbol = input[position[0]][position[1]]
  steps += 1

iterate_needed = True
while iterate_needed:
  iterate_needed = False
  for i, row in enumerate(twin):
    for j, p in enumerate(row):
      if twin[i][j] == 'O' :
        if i-1 >= 0 and twin[i-1][j] == '.':
          twin[i-1][j] = 'O'
          iterate_needed = True
        if j+1 < len(twin[0]) and twin[i][j+1] == '.':
          twin[i][j+1] = 'O'
          iterate_needed = True
        if i+1 < len(twin) and twin[i+1][j] == '.':
          twin[i+1][j] = 'O'
          iterate_needed = True
        if j-1 >= 0 and twin[i][j-1] == '.':
          twin[i][j-1] = 'O'
          iterate_needed = True

# count I
count = sum(row.count(".") for row in twin)
print(count)