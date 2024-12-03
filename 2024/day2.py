import re
from utils import read_input

def check_reports(r):
    safe = -1
    increasing = 1 if r[0] < r[1] else -1
    for i,l in enumerate(r):
        if i == len(r) - 1:
            break
        if not (r[i]*increasing < r[i+1]*increasing and not r[i] == r[i+1] and abs(r[i] - r[i+1]) < 4):
            safe = i
            break
    return safe

data = read_input("day2.txt")
reports = []
for d in data:
    report = [int(x) for x in re.findall(r'\d+', d)]
    reports.append(report)

safe_reports = 0
for r in reports:
    safe_reports += 1 if check_reports(r) == -1 else 0

print(safe_reports)

safe_reports = 0
for r in reports:
    safe_report = check_reports(r)
    if safe_report == -1:
        safe_reports += 1
    else:
        r_1 = r.copy()
        r_2 = r.copy()
        del r_1[safe_report]
        del r_2[safe_report+1]
        if check_reports(r_1) == -1 or check_reports(r_2) == -1:
            safe_reports += 1
        
print(safe_reports)
