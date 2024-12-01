import re
from collections import Counter
from utils import read_input

# Open file day1.txt in read mode

data = read_input("day1.txt")

list_1, list_2 = zip(*[[int(x) for x in re.findall(r'\d+', d)] for d in data])

list_1 = sorted(list_1)
list_2 = sorted(list_2)

result_part1 = sum(abs(a-b) for a, b in zip(list_1, list_2))
print(result_part1)

result_part2 = 0
counter = Counter(list_2)

for l_1 in list_1:
    result_part2 += counter[l_1] * l_1

print(result_part2)
