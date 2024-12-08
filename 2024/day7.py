from utils import read_input
import re

data = read_input("day7.txt")

equations = []
for d in data:
  equations.append([int(x) for x in re.findall(r'\d+', d)])

result_part1,result_part2 = 0,0

for e in equations:
  r = e[0]
  vals = e[1:]
  operator = ["+"] * (len(vals)-1)
  trying = True
  while trying:
    r_temp = e[1]
    for vs,ops in zip(vals[1:],operator):
      if ops == "+":
        r_temp += vs
      elif ops == "*":
        r_temp *= vs
      if r_temp > r:
        break
    if r == r_temp:
      result_part1 += r
      break
    else:
      i = 0
      while True:
        if operator[i] == "+":
          operator[i] = "*"
          break
        else:
          operator[i] = "+"
        i += 1
        if i == len(operator):
          trying = False
          break
        
print(result_part1)

# 20281182715321 correct

for e in equations:
  r = e[0]
  vals = e[1:]
  operator = ["+"] * (len(vals)-1)
  trying = True
  while trying:
    vals_temp = vals.copy()
    oper_temp = operator.copy()
    remove_from_oper = []
    r_temp = vals_temp[0]
    for vs,ops in zip(vals_temp[1:],oper_temp):
      if ops == "+":
        r_temp += vs
      elif ops == "*":
        r_temp *= vs
      elif ops == "||":
        r_temp = int(str(r_temp)+str(vs))
      if r_temp > r:
        break
    # print(e,operator,vals_temp,oper_temp,r_temp,r == r_temp,remove_from_oper)
    if r == r_temp:
      result_part2 += r
      break
    else:
      i = 0
      while True:
        if operator[i] == "+":
          operator[i] = "*"
          operator[:i] = ["+"]*i
          break
        elif operator[i] == "*":
          operator[i] = "||"
          operator[:i] = ["+"]*i
          break
        else:
          operator[i] == "+"
        i += 1
        if i == len(operator):
          trying = False
          break
        
print(result_part2)

# 28341556255615 is too low