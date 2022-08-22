import sys, re

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r'\b(\w)(\w)', r'\2\1', line)
    print(line)