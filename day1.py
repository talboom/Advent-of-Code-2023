import os
from utils import read_input
# Open file day1.txt in read mode


data = read_input("day1.txt")


# function that removes all letter from string
def remove_letters(s):
    return "".join([i for i in s if i.isdigit()])

# function to replace string one to o1ne, two to t2wo, three to t3ree ...
def replace_written_numbers(s):
    s = s.replace('one', 'o1ne')
    s = s.replace('two', 't2wo')
    s = s.replace('three', 't3ree')
    s = s.replace('four', 'f4our')
    s = s.replace('five', 'f5ive')
    s = s.replace('six', 's6ix')
    s = s.replace('seven', 's7even')
    s = s.replace('eight', 'e8ight')
    s = s.replace('nine', 'n9ine')
    return s

# Loop trough list of string and return first and last number of each string
sum_res = 0
for d in data:
    numbers = remove_letters(d)
    # make digits
    first = int(numbers[0]+numbers[-1])
    sum_res += first

print(sum_res)

# Loop trough list of string and return first and last number of each string
sum_res = 0
for d in data:
    d = replace_written_numbers(d)
    numbers = remove_letters(d)
    # make digits
    first = int(numbers[0]+numbers[-1])
    sum_res += first

print(sum_res)