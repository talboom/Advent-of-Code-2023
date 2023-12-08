from utils import read_input
from collections import namedtuple, defaultdict
import re

Hand = namedtuple('Hand', ['red', 'green', 'blue'])

limits = {
  'red': 12,
  'green': 13,
  'blue': 14
}

input = read_input("day2.txt")


res_sum = 0 
for i, line in enumerate(input):
  valid_game = True
  for hand in line.split(":")[-1].split(";"):
      for color, value in limits.items():
         if match := re.search(r'\d+ ' + color, hand):
            if int(match[0].split(' ')[0]) > value:
               valid_game = False

  if valid_game:
      res_sum += i+1

print(res_sum)

res_sum = 0 
for i, line in enumerate(input):
  valid_game = True

  min_cubes = defaultdict(lambda: None)

  for color, value in limits.items():
      if not color in line:
         valid_game = False
  for hand in line.split(":")[-1].split(";"):
      for color in limits.keys():
         if match := re.search(r'\d+ ' + color, hand):
            if min_cubes[color] is None or int(match[0].split(' ')[0]) > min_cubes[color]: 
                min_cubes[color] = int(match[0].split(' ')[0])

  product_res = 1
  for value in min_cubes.values():
      product_res *= value
  res_sum += valid_game * product_res
print(res_sum)