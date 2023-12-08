from utils import read_input
from collections import defaultdict
import re

input = read_input("day3.txt")

sum_part_numbers = 0

for i,line in enumerate(input):
  for match in re.finditer(r'(\ )', line):
    number = int(match.group())
    start = match.start()
    end = match.end()

    valid_part = False

    start_line = max(i-1, 0)
    end_line = min(i+2, len(input))

    start_pos = max(0, start-1)
    end_pos = min(len(line), end+1)
    for rel_line in input[start_line:end_line]:
      check_line = rel_line[start_pos:end_pos]
      for l in rel_line[start_pos:end_pos]:
        if l != "." and not l.isdigit():
          valid_part = True
          break
      if valid_part:
        break
    sum_part_numbers += number if valid_part else 0
    
print(sum_part_numbers)

sum_gear_ratio = 0
gears = defaultdict(int)


for i, line in enumerate(input):
  for match in re.finditer(r'(\d+)', line):
    number = int(match.group())
    start = match.start()
    end = match.end()

    valid_part = False

    start_line = max(i-1, 0)
    end_line = min(i+2, len(input))

    start_pos = max(0, start-1)
    end_pos = min(len(line), end+1)
    for j, rel_line in enumerate(input[start_line:end_line]):
      check_line = rel_line[start_pos:end_pos]
      for k,l in enumerate(rel_line[start_pos:end_pos]):
        if l == '*':
          if (prev := gears[(start_line+j,start_pos+k)]) == 0:
            gears[(start_line+j,start_pos+k)] = [number]
          else:
            gears[(start_line+j,start_pos+k)].append(number)
            sum_gear_ratio +=  prev[0]*number


sum_gear_ratio_2 = 0

for val in gears.values():
  product = 1
  if len(val) > 1:
    for v in val:
      product *= v
    sum_gear_ratio_2 += product
    

print(sum_gear_ratio)
print(sum_gear_ratio_2)