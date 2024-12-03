import re
from collections import Counter
from utils import read_input

data = read_input("day3.txt")

muls = [re.findall(r'mul\((\d{1,3})\,(\d{1,3})\)', d) for d in data]

result_part1 = 0
for mul in muls:
  result_part1 += sum(int(a)*int(b) for a, b in mul)

print(result_part1)


muls = [re.findall(r'mul\((\d{1,3})\,(\d{1,3})\)|(do\(\))|(don\'t\(\))', d) for d in data]

result_part2 = 0
times = 1
for mul in muls:
  for m in mul:
    a,b,c,d = m
    if d == 'don\'t()':
      times = 0
    elif c == 'do()':
      times = 1
    else:
      result_part2 += int(a)*int(b)*times

print(result_part2)
