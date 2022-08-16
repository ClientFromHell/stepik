import sys, re

for line in sys.stdin:
    line = line.rstrip()
    if re.fullmatch(r'(1(01*0)*1|0)*', line):
        print(line)


