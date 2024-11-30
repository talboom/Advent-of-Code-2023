from utils import read_input

input = read_input("day18_test.txt")
plan = [[l[0],int(l[1])] for l in [l.split(" ") for l in input]]

h,w,h2,w2,h3,w3 = 0,0,0,0,0,0
for step in plan:
    if step[0] == "R":
        w += step[1]
        w2 = max(w,w2)
    elif step[0] == "L":
        w -= step[1]
        w3 = min(w,w3)
    elif step[0] == "D":
        h += step[1]
        h2 = max(h,h2)
    elif step[0] == "U":
        h -= step[1]
        h3 = min(h,h3)
h = h2 - h3 + 1
w = w2 - w3 + 1

terrain = [["." for i in range(w)] for j in range(h)]
dig = (-h3,-w3)
terrain[-h3][-w3] = "#"

for s in plan:
    if s[0] == "R":
        terrain[dig[0]][dig[1]] = "U"
        terrain[dig[0]][dig[1]+s[1]] = "D"	
        dig = (dig[0],dig[1]+s[1])
    elif s[0] == "L":
        terrain[dig[0]][dig[1]-s[1]] = "U" 
        terrain[dig[0]][dig[1]] = "D"
        dig = (dig[0],dig[1]-s[1])
    elif s[0] == "D":
        for i in range(1,s[1]+1):
            terrain[dig[0]+i][dig[1]] = "D"
        dig = (dig[0]+s[1],dig[1])
    elif s[0] == "U":
        for i in range(1,s[1]+1):
            terrain[dig[0]-i][dig[1]] = "U"	
        dig = (dig[0]-s[1],dig[1])

# Guess inside
terrain[-h3+1][-w3+1] = "I"

iterate_needed = True
while iterate_needed:
  iterate_needed = False
  for i, row in enumerate(terrain):
    for j, p in enumerate(row):
      if terrain[i][j] == 'I' :
        if i-1 >= 0 and terrain[i-1][j] == '.':
          terrain[i-1][j] = 'I'
          iterate_needed = True
        if j+1 < len(terrain[0]) and terrain[i][j+1] == '.':
          terrain[i][j+1] = 'I'
          iterate_needed = True
        if i+1 < len(terrain) and terrain[i+1][j] == '.':
          terrain[i+1][j] = 'I'
          iterate_needed = True
        if j-1 >= 0 and terrain[i][j-1] == '.':
          terrain[i][j-1] = 'I'
          iterate_needed = True

print(sum([sum([1 if s == "#" or s == "I" else 0 for s in r]) for r in terrain]))
sum = 9
for i, row in enumerate(terrain):
  print(row)
  l = []
  r = []
  for j, p in enumerate(row):
    if terrain[i][j] == 'U':
      l.append(j)
    if terrain[i][j] == 'D':
      r.append(j)
  for k in range(len(l)):
    sum += r[k]-l[k]
      

# function that finds char in array
def find(array, char):
    for i, row in enumerate(array):
        for j, p in enumerate(row):
            if p == char:
                return (i,j)
# function that finds char in string
def find_string(string, char):
    for i, row in enumerate(string):
        for j, p in enumerate(row):
            if p == char:
                return (i,j)
       
## Part 2

