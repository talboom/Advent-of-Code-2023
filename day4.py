from utils import read_input
from collections import defaultdict
import re

input = read_input("day4.txt")

answer_part1 = 0

for line in input:
  numbers_array =  line.split(":")[-1].split("|")
  numbers_elf = [int(x) for x in re.findall(r'\d+', numbers_array[0])]
  numbers_winner = [int(x) for x in re.findall(r'\d+', numbers_array[1])]
  
  card_points = 0
  
  for n in numbers_elf:
    if n in numbers_winner:
      card_points = max(card_points*2,1) 
  answer_part1 += card_points

print(answer_part1)


answer_part2 = len(input)
multiplier = defaultdict(int)
multiplier.default_factory = lambda: 1

for i, line in enumerate(input):
  numbers_array =  line.split(":")[-1].split("|")
  numbers_elf = [int(x) for x in re.findall(r'\d+', numbers_array[0])]
  numbers_winner = [int(x) for x in re.findall(r'\d+', numbers_array[1])]
  
  cards = 0
  j = 1
  for n in numbers_elf:
    if n in numbers_winner:
        cards += 1
        multiplier[i+1+j] += 1* multiplier[i+1]
        j += 1
  cards = cards * multiplier[i+1]
  answer_part2 += cards

print(answer_part2)