from utils import read_input
import re
import math

lines = read_input("day7.txt")
hands = [[x[0], int(x[1])] for h in lines for x in [h.split()]]

def hand_type(hand):
  char_dict = {}
  for char in hand:
      if char in char_dict:
          char_dict[char] += 1
      else:
          char_dict[char] = 1
  
  if max(char_dict.values()) == 5:
    return 7
  elif max(char_dict.values()) == 4:
    return 6
  elif 3 in char_dict.values() and 2 in char_dict.values():
    return 5
  elif 3 in char_dict.values():
    return 4
  elif 2 in char_dict.values() and len(char_dict.values()) == 3:
    return 3
  elif 2 in char_dict.values():
    return 2
  else:
    return 1

scores = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}


for i, hand in enumerate(hands):
  c_scores = []
  for c in hand[0]:
    c_scores.append(scores[c])
  hands[i] = hands[i]+c_scores
      

hands_sorted = sorted(hands, key=lambda x: (hand_type(x[0]),x[2],x[3],x[4],x[5],x[6]))
part_1 = 0
for i, h in enumerate(hands_sorted):
   part_1 += h[1] *(i+1) 
print(part_1)


hands = [[x[0], int(x[1])] for h in lines for x in [h.split()]]


def hand_type2(hand):
  char_dict = {}
  for char in hand:
      if char in char_dict:
          char_dict[char] += 1
      else:
          char_dict[char] = 1
  if 'J' in char_dict and char_dict['J'] < 5:
    max_key, max_value = max(char_dict.items(), key=lambda x: (x[0] != 'J',x[1]))
    char_dict[max_key] += char_dict['J']
    char_dict.pop('J')
  if max(char_dict.values()) == 5:
    return 7
  elif max(char_dict.values()) == 4:
    return 6
  elif 3 in char_dict.values() and 2 in char_dict.values():
    return 5
  elif 3 in char_dict.values():
    return 4
  elif 2 in char_dict.values() and len(char_dict.values()) == 3:
    return 3
  elif 2 in char_dict.values():
    return 2
  else:
    return 1

scores = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}

for i, hand in enumerate(hands):
  c_scores = []
  for c in hand[0]:
    c_scores.append(scores[c])
  hands[i] = hands[i]+c_scores
      

hands_sorted = sorted(hands, key=lambda x: (hand_type2(x[0]),x[2],x[3],x[4],x[5],x[6]))
part_2 = 0
for i, h in enumerate(hands_sorted):
   part_2 += h[1] *(i+1) 
print(part_2)