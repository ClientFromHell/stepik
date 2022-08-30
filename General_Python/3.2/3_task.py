import sys, re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r'z\w\w\wz', line):
        print(line)