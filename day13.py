from utils import read_input

input = read_input("day13_test.txt")

puzzles = []
puzzle = []
for line in input:
  if line == "":
    puzzles.append(puzzle)
    puzzle = []
  else:
    puzzle.append(line)

sum_mirrors = 0

for puzzle in puzzles:
  # check for horizontal mirror
  for i in range(1,len(puzzle)):
    size = min(i,len(puzzle[0]-i))
    for j in range(0,size):
      if puzzle[i-j-1] == puzzle[i+j]:
        sum_mirrors += 1
      else:
        break 
  