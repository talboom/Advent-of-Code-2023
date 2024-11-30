from utils import read_input
import re
import math

lines = read_input("day6.txt")

# read lines
times = [x for x in re.findall(r'\d+', lines[0])]
distances = [x for x in re.findall(r'\d+', lines[1])]

times_one = int("".join(times))
distances_one = int("".join(distances))

times_int = [int(x) for x in times] 
distances_int = [int(x) for x in distances]

num_of_ways = []
for t ,d in zip(times_int,distances_int):

  a = -1
  b = t
  c = -d
  discriminant = b**2 - 4*a*c  
  if discriminant <= 0:
    print("Huh?")
  x1 = math.floor((-b + math.sqrt(discriminant)) / (2*a))
  x2 = math.floor((-b - math.sqrt(discriminant)) / (2*a))
  if (t - x1)*(x1) == d:
    x1 += 1
  num_of_ways.append(x2-x1)  


product = 1
for i in num_of_ways:
  product *= i

print(product)


t ,d = times_one,distances_one

a = -1
b = t
c = -d
discriminant = b**2 - 4*a*c  
if discriminant <= 0:
  print("Huh?")
x1 = math.floor((-b + math.sqrt(discriminant)) / (2*a))
x2 = math.floor((-b - math.sqrt(discriminant)) / (2*a))
if (t - x1)*(x1) == d:
  x1 += 1
print(x2-x1)  
