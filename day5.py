from utils import read_input
from collections import defaultdict
import re



def map_source_to_destination(map, number):
  result = list(filter(lambda x: number >= x[1] and number < x[1]+x[2], map))
  if len(result) == 0:
    return number
  return number + result[0][0] - result[0][1]  


lines = read_input("day5.txt")

seeds = [int(x) for x in re.findall(r'\d+', lines[0])]

maps = {}
maps_rev = {}
maps_values = defaultdict(list)
maps_values.default_factory = lambda: []
maps_values_rev = defaultdict(list)
maps_values_rev.default_factory = lambda: []

for line in lines[2:]:
  if len(line) < 1:
    do_nothing = True
  elif not line[0].isdigit():
    source_name,destination_name  = line[0:-5].split("-to-")
    maps[source_name] = destination_name
  else:
    maps_values[source_name].append([int(x) for x in re.findall(r'\d+', line)])

result = None

for s in seeds:
  value = s
  source = 'seed'  
  while source != 'location':
    value = map_source_to_destination(maps_values[source],value)
    source = maps[source]
  if result == None or result > value:
    result = value
print(result)


# part 2
def map_source_to_destination_range(map, source_range):

  results = list(filter(lambda x: 
                       (source_range[0] >= x[1] and source_range[0] < x[1]+x[2]) or
                       (source_range[1] >= x[1] and source_range[1] < x[1]+x[2]) or
                       (source_range[0] < x[1] and source_range[1] >= x[1]+x[2])
                       , map))
  sorted_m_results = sorted(results, key=lambda x: x[1])
  if len(sorted_m_results) == 0:
    results += [[source_range[0], source_range[0],source_range[1]-source_range[0]+1]]
  else:
    if source_range[0] < sorted_m_results[0][1]:
      start = source_range[0]
      results += [[start, start,sorted_m_results[0][1]-source_range[0]]]
    if source_range[1] > sorted_m_results[-1][1]+sorted_m_results[-1][2]:
      end = sorted_m_results[-1][1]+sorted_m_results[-1][2]
      results += [[end, end, source_range[1]-end]]
  ranges = []
  for r in results:
    ranges += [map_source_to_destination_single_range(r, source_range)]
  return ranges

def map_source_to_destination_single_range(single_map, source_range):
  min_range = max(
    single_map[1],
    source_range[0]
  )
  max_range = min(
    single_map[1]+single_map[2]-1,
    source_range[1]
  )
  min_dest = map_source_to_destination([single_map], min_range)
  max_dest = map_source_to_destination([single_map], max_range)
  return [min_dest, max_dest]

seed_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

for m_key in maps_values.keys():
  sorted_m_value = sorted(maps_values[m_key], key=lambda x: x[1])
  maps_values[m_key] = sorted_m_value

vals = []
for seed_range in seed_ranges:
  value = s
  source = 'seed'
  source_range =[[seed_range[0],seed_range[0]+seed_range[1]]]
  while source != 'location':
    new_source_range = []
    for single_range in source_range:
      new_source_range += map_source_to_destination_range(maps_values[source],single_range)
    source = maps[source]
    source_range = new_source_range
  first_values = list(map(lambda x: x[0], source_range))
  min_value = min(first_values)
  vals.append(min_value)
print(min(vals))