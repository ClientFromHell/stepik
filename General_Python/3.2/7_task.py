import sys, re

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(r"\b[a|A]+\b", "argh", line, 1)
    print(line)
