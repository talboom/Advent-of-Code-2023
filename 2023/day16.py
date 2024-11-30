from utils import read_input

input = read_input("day16.txt")

field = []

for line in input:

  field.append([x for x in line])

energized = [[0]*len(field[0]) for _ in range(len(field))]
energized_dir =  [[[0,0,0,0]]*len(field[0]) for _ in range(len(field))]
# part 1 beam
beams = [
  {'dir':[0,1,0,0],
  'pos':[0,-1]}
  ]

new_beams = []

while len(beams) > 0:
  for nb in new_beams:
    beams.append(nb)
  new_beams = []
  for i, beam in enumerate(beams):
    # next position
    ver = beam["pos"][0] + beam["dir"][2]-beam["dir"][0]
    hor = beam["pos"][1] + beam["dir"][1]-beam["dir"][3]

    # new position is out of bounds or already energized
    if ver < 0 or ver >= len(field) or hor < 0 or hor >= len(field[0]):
      beams.pop(i)
      continue
    elif energized_dir[ver][hor][beam["dir"].index(1)] == 1: # already energized to the max
      beams.pop(i)
      continue
      

    # energize
    energized[ver][hor] += 1
    energized_dir[ver][hor] = [a + b for a, b in zip(energized_dir[ver][hor], beam["dir"])]

    # Get new direction
    if field[ver][hor] == ".":
      new_dir = beam["dir"]
    elif field[ver][hor] == "|" and (beam["dir"][0] == 1 or beam["dir"][2] == 1):
      new_dir = beam["dir"]
    elif field[ver][hor] == "-" and (beam["dir"][1] == 1 or beam["dir"][3] == 1):
      new_dir = beam["dir"]
    elif field[ver][hor] == "/":
      new_dir = beam["dir"][:2][::-1] + beam["dir"][2:][::-1]
    elif field[ver][hor] == "\\":
      new_dir = beam["dir"][2:][::-1] + beam["dir"][:2][::-1]
    elif field[ver][hor] == "|" and (beam["dir"][1] == 1 or beam["dir"][3] == 1):
      new_dir = [1,0,0,0]
      new_beams.append({'dir':[0,0,1,0],'pos':[ver,hor]})
    elif field[ver][hor] == "-" and (beam["dir"][0] == 1 or beam["dir"][2] == 1):
      new_dir = [0,1,0,0]
      new_beams.append({'dir':[0,0,0,1],'pos':[ver,hor]})
    else:
      print("error")
    
    
    beams[i]["pos"] = [ver,hor]
    beams[i]["dir"] = new_dir

part_1 = len(field)*len(field[0]) - sum([x.count(0) for x in energized])
print(part_1)



# part 2 beams
opt_beams = []
# from north and south
for i in range(len(field[0])):
  opt_beams.append(
    {'dir':[0,0,1,0],
    'pos':[-1,i]}
  ) 
  opt_beams.append(
    {'dir':[1,0,0,0],
    'pos':[len(field),i]}
  )
# from west and east
for i in range(len(field)):
  opt_beams.append(
    {'dir':[0,0,0,1],
    'pos':[i,len(field[0])]}
  ) 
  opt_beams.append(
    {'dir':[0,1,0,0],
    'pos':[i,-1]}
  )


part2 = 0

for b in opt_beams:
  beams = [b]
  new_beams = []

  energized = [[0]*len(field[0]) for _ in range(len(field))]
  energized_dir =  [[[0,0,0,0]]*len(field[0]) for _ in range(len(field))]

  while len(beams) > 0:
    for nb in new_beams:
      beams.append(nb)
    new_beams = []
    for i, beam in enumerate(beams):
      # next position
      ver = beam["pos"][0] + beam["dir"][2]-beam["dir"][0]
      hor = beam["pos"][1] + beam["dir"][1]-beam["dir"][3]

      # new position is out of bounds or already energized
      if ver < 0 or ver >= len(field) or hor < 0 or hor >= len(field[0]):
        beams.pop(i)
        continue
      elif energized_dir[ver][hor][beam["dir"].index(1)] == 1: # already energized to the max
        beams.pop(i)
        continue
        

      # energize
      energized[ver][hor] += 1
      energized_dir[ver][hor] = [a + b for a, b in zip(energized_dir[ver][hor], beam["dir"])]

      # Get new direction
      if field[ver][hor] == ".":
        new_dir = beam["dir"]
      elif field[ver][hor] == "|" and (beam["dir"][0] == 1 or beam["dir"][2] == 1):
        new_dir = beam["dir"]
      elif field[ver][hor] == "-" and (beam["dir"][1] == 1 or beam["dir"][3] == 1):
        new_dir = beam["dir"]
      elif field[ver][hor] == "/":
        new_dir = beam["dir"][:2][::-1] + beam["dir"][2:][::-1]
      elif field[ver][hor] == "\\":
        new_dir = beam["dir"][2:][::-1] + beam["dir"][:2][::-1]
      elif field[ver][hor] == "|" and (beam["dir"][1] == 1 or beam["dir"][3] == 1):
        new_dir = [1,0,0,0]
        new_beams.append({'dir':[0,0,1,0],'pos':[ver,hor]})
      elif field[ver][hor] == "-" and (beam["dir"][0] == 1 or beam["dir"][2] == 1):
        new_dir = [0,1,0,0]
        new_beams.append({'dir':[0,0,0,1],'pos':[ver,hor]})
      else:
        print("error")
      
      
      beams[i]["pos"] = [ver,hor]
      beams[i]["dir"] = new_dir

  result = len(field)*len(field[0]) - sum([x.count(0) for x in energized])
  part2 = max(part2, result)

print(part2)
# Wrong answer: 8695