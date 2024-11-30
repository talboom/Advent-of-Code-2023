from utils import read_input

input = read_input("day11.txt")

add_rows = []
add_cols = [x for x in range(len(input))]
galaxies = []

for i, line in enumerate(input):
  if line.find('#') == -1:
    add_rows.append(i)
  else:
    for j, char in enumerate(line):
      if char == '#':
          galaxies.append([i,j])
          if j in add_cols:
            add_cols.remove(j)

# part 1: space_size = 2
# part 2: space_size = 1000000
space_size = 1000000
steps = 0
for i, galaxy in enumerate(galaxies):
  for j in range(i):
    galaxy2 = galaxies[j]
    count_rows = len([num for num in add_rows if min(galaxy2[0],galaxy[0]) <= num < max(galaxy2[0],galaxy[0])])
    count_cols = len([num for num in add_cols if min(galaxy2[1],galaxy[1]) <= num < max(galaxy2[1],galaxy[1])])
    steps += abs(galaxy2[0]-galaxy[0]) + abs(galaxy2[1]-galaxy[1]) + (count_rows + count_cols)*(space_size-1)
print(steps)
