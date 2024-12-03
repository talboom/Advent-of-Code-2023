import re
from utils import read_input

data = read_input("day3.txt")

muls = [re.findall(r'mul\((\d{1,3})\,(\d{1,3})\)', d) for d in data]

result_part1 = 0
for mul in muls:
  result_part1 += sum(int(a)*int(b) for a, b in mul)

print(result_part1)


muls = [re.findall(r'mul\((\d{1,3})\,(\d{1,3})\)|(do\(\))|(don\'t\(\))', d) for d in data]

result_part2 = 0
enable = 1
for mul in muls:
  for m in mul:
    a,b,c,d = m
    if d == 'don\'t()':
      enable = 0
    elif c == 'do()':
      enable = 1
    else:
      result_part2 += int(a)*int(b)*enable

print(result_part2)
