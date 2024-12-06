from utils import read_input

data = read_input("day6.txt")

map = [list(d) for d in data]

map_height = len(map)
map_width = len(map[0])

for x,r in enumerate(map):
  if "^" in r:
    for y,c in enumerate(r):
      if c == "^":
        guard = [x,y]

directions = [[-1,0],[0,1],[1,0],[0,-1]]
d = 0
steps = 0
map[guard[0]][guard[1]] = "X"
while 0 <= guard[0]+directions[d][0] < map_height and 0 <= guard[1]+directions[d][1] < map_width:
  guard[0] += directions[d][0]
  guard[1] += directions[d][1]
  steps += 1
  if map[guard[0]][guard[1]] == "#":
    guard[0] -= directions[d][0]
    guard[1] -= directions[d][1]
    d = (d + 1) % 4
    guard[0] += directions[d][0]
    guard[1] += directions[d][1]
  map[guard[0]][guard[1]] = "X"

print(sum([row.count("X") for row in map]))

# Solution part 2
# 1. Make 4 maps for each direction
# 2. make sure you fill the maps with the direction of the guard plus add the tiles if he would turn left (and walk backwards)
# 3. Let the guard do a round and count how often he passes a cross that would lead him to a repeating path
# 4. do this in sequence to make sure it isn't a "future" path (and thus shortning his distance to the end of the map)