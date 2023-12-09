from utils import read_input
import re

input = read_input("day9.txt")
sequences = []
for line in input:
  sequences.append([int(x) for x in re.findall(r'-?\d+', line)])

# simple
part_1 = 0
for s in sequences:
  levels = [s]
  while max(levels[-1]) != 0 or min(levels[-1]) != 0:
    next_level = []
    for i, number in enumerate(levels[-1][:-1]):
      next_level.append(levels[-1][i+1]-levels[-1][i])
    levels.append(next_level)
  addition = levels[-1][-1]
  for j, s in enumerate(reversed(levels[:-1])):
      levels[-j-2].append(s[-1]+addition)
      addition = levels[-j-2][-1]
  part_1 += levels[0][-1]
print(part_1)

# simple
part_2 = 0
for s in sequences:
  levels = [[0]+s]
  while max(levels[-1]) != 0 or min(levels[-1]) != 0:
    next_level = []
    for i, number in enumerate(levels[-1][1:-1]):
      next_level.append(levels[-1][i+2]-levels[-1][i+1])
    levels.append([0]+next_level)
  addition_start = levels[-1][-1]
  addition_end = levels[-1][0]
  for j, s in enumerate(reversed(levels[:-1])):
      levels[-j-2][0]= (s[1]-addition_start)
      levels[-j-2].append(s[-1]+addition_end)
      addition_start = levels[-j-2][0]
      addition_end = levels[-j-2][-1]
  part_2 += levels[0][0]
print(part_2)