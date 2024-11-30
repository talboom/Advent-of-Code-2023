from utils import read_input
import re
import math

lines = read_input("day8.txt")
instructions = lines[0]
nodes = {}
start_positions = []
end_positions = []
for l in lines[2:]:
  sep_line = [x for x in re.findall(r'\b[A-Z0-9]{3}\b', l)]
  nodes[sep_line[0]] = sep_line[1:]
  if sep_line[0][2] == "A":
    start_positions.append(sep_line[0])
  if sep_line[0][2] == "Z":
    end_positions.append(sep_line[0])

print(start_positions)

position = "AAA"
i = 0
while position != "ZZZ":
  next_step = instructions[i % len(instructions)]
  if next_step == "L":
    position = nodes[position][0]
  elif next_step == "R":
    position = nodes[position][1]
  i += 1
print(i)


steps = []
for position in start_positions:
  i = 0
  while position[2] != "Z":
    next_step = instructions[i % len(instructions)]
    if next_step == "L":
      position = nodes[position][0]
    elif next_step == "R":
      position = nodes[position][1]
    i += 1
  steps.append(i)

print(math.lcm(*steps))
