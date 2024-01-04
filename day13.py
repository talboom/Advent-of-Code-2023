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
puzzles.append(puzzle)

mirrors = [0,0]

for puzzle in puzzles:
  # check for horizontal mirror
  for i in range(1,len(puzzle)):
    size = min(i,len(puzzle)-i)
    mirror = True
    for j in range(0,size):
      if puzzle[i-j-1] != puzzle[i+j]:
        mirror = False
        break 
    if mirror:
      mirrors[0] += i
      break
  # check for vertical mirror
  for i in range(1,len(puzzle[0])):
    size = min(i,len(puzzle[0])-i)
    mirror = True
    end = i+size
    for j in range(0,len(puzzle)):
      if puzzle[j][i-size:i] != puzzle[j][i:i+size][::-1]:
        mirror = False
        break
    if mirror:
      mirrors[1] += i
      break

print(mirrors[0]*100+mirrors[1]*1)



mirrors = [0,0]

for puzzle in puzzles:
  # check for horizontal mirror
  for i in range(1,len(puzzle)):
    size = min(i,len(puzzle)-i)
    mirror = True
    smudge = []
    for j in range(0,size):
      if puzzle[i-j-1] != puzzle[i+j] and len(smudge) == 1:
        mirror = False
        break 
      elif puzzle[i-j-1] != puzzle[i+j]:
        for c in range(len(puzzle[i-j-1])):
          if puzzle[i-j-1][c] != puzzle[i+j][c]:
            smudge.append([i-j-1,c])
          if len(smudge) > 1:
            mirror = False
            break
      if mirror == False:
        break
    if mirror:
      mirrors[0] += i
      print(smudge)
      break
  # check for vertical mirror
  for i in range(1,len(puzzle[0])):
    size = min(i,len(puzzle[0])-i)
    mirror = True
    smudge = []
    end = i+size
    for j in range(0,len(puzzle)):
      if puzzle[j][i-size:i] != puzzle[j][i:i+size][::-1] and len(smudge) == 1:
        mirror = False
        break
      elif puzzle[j][i-size:i] != puzzle[j][i:i+size][::-1]:
       for c in range(size):
          if puzzle[j][i-c-1] != puzzle[j][i+c]:
            smudge.append([j,i-size-c])
          if len(smudge) > 1:
            mirror = False
            break
      if mirror == False:
        break
    if mirror:
      mirrors[1] += i
      print(smudge)
      break

print(mirrors[0]*100+mirrors[1]*1)