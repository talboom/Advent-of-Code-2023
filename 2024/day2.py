import re
from utils import read_input

def check_reports(r):
    safe = -1
    check_starting_two = False
    increasing = 1 if r[0] < r[1] else -1
    for i,l in enumerate(r):
        if i == len(r) - 1:
            break
        if not (r[i]*increasing < r[i+1]*increasing and abs(r[i] - r[i+1]) < 4):
            safe = i
            if not r[i]*increasing < r[i+1]*increasing:
                check_starting_two = True
            break
    return safe,check_starting_two

data = read_input("day2.txt")
reports = []
for d in data:
    report = [int(x) for x in re.findall(r'\d+', d)]
    reports.append(report)

safe_reports = 0
for r in reports:
    safe_reports += 1 if check_reports(r)[0] == -1 else 0

print(safe_reports)

safe_reports = 0
for r in reports:
    safe_report,check_starting_two = check_reports(r)
    if safe_report == -1:
        safe_reports += 1
    else:
        for i in range(len(r)):
            if check_reports(r[:i]+r[i+1:])[0] == -1:
                safe_reports += 1
                break
                
        
print(safe_reports)
