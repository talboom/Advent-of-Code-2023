import re
from utils import read_input
def check_order(update,rev_order):
  correct = True
  for i,u in enumerate(update):
    if u in rev_order:
      for v in rev_order[u]:
        if v in update[i+1:]:
          correct = False
          break
  return correct

data = read_input("day5.txt")

first_section = True
order,rev_order = {},{}
updates, starts, ends = [],[],[]

for d in data:
  if d == '':
    first_section = False
  elif first_section:
    start,end = [int(x) for x in re.findall(r'\d+', d)]
    if start in order:
      order[start].append(end)
    else:
      order[start] = [end]
    
    if end in rev_order:
      rev_order[end].append(start)
    else:
      rev_order[end] = [start]

    starts.append(start)
    ends.append(end)
  else:
    updates.append([int(x) for x in re.findall(r'\d+', d)])

incorrect_ordered = []

result_part1 = 0
for update in updates:
  unordered = check_order(update,rev_order)        
  if unordered:
    result_part1 += update[int((len(update)-1)/2)]
  else:
    incorrect_ordered.append(update)
          
print(result_part1)

result_part2 = 0

for update in incorrect_ordered:
  unordered = True
  while unordered:
    for i,u in enumerate(update):
      if u in rev_order:
        for v in rev_order[u]:
          if v in update[i+1:]:
            update.remove(v)
            update = update[:i] + [v] + update[i:]
    unordered = not check_order(update,rev_order)
  result_part2 += update[int((len(update)-1)/2)]

print(result_part2)

# 5184 correct