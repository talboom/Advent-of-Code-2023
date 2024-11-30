import re

from utils import read_input


def parse_map_part(map_part):
    return [
        [int(i) for i in instruction] 
        for line in map_part
        if (instruction := re.findall(r'\d+', line))
    ]
    
            


def parse_map(map):
    seeds = [int(i) for i in re.findall(r'\d+', map[0])]

    map_parts, map_part = [], []
    for row in map[3:]:
        if row != '':
            map_part.append(row)
        else:
            map_parts.append(parse_map_part((map_part)))
            map_part = []
    map_parts.append(parse_map_part((map_part)))

    return seeds, map_parts


def part1(seeds, parsed_map):
    seed_nrs = []
    for seed in seeds:
        next_seed = seed
        for map_part in parsed_map:
            for destination, source, range_length in map_part:
                if set([next_seed]) & set(range(source, source+range_length)):
                    difference = destination - source
                    next_seed = next_seed + difference
                    break
        seed_nrs.append(next_seed)
    print(min(seed_nrs))


if __name__ == '__main__':
    file_input = read_input('day5.txt')
    part1(*parse_map(file_input))