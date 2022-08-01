import collections, sys

DICT_CLASS = {}
CLS_CHECKER = []
inherit = []
elements = []
RESULTS = []

visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue
res = []


def bfs(visited, graph, node):
    visited.append(node)
    for i in graph[node]:
        if i in graph:
            bfs(visited, graph, i)
        else:
            visited.append(i)
    return visited


for i in range(int(sys.stdin.readline().strip())):
    inherit.append([num for num in filter(lambda num: num.isalpha(), sys.stdin.readline().strip())])
#
for i in range(int(sys.stdin.readline())):
    CLS_CHECKER.append(sys.stdin.readline().strip().split())

i_test = []

for i in inherit:
    i_test.append([num for num in filter(lambda num: num.isalpha(), i)])

for i in i_test:
    elements += i
    if len(i) == 1:
        DICT_CLASS[i[0]] = []
    else:
        DICT_CLASS[i[0]] = i[1:]

elements = set(elements)

for i in CLS_CHECKER:
    res = []
    visited = []
    if i[0] not in elements or i[-1] not in elements:
        RESULTS.append('No')
    elif i[0] == i[-1]:
        RESULTS.append('Yes')
    else:
        res = bfs(visited, DICT_CLASS, i[-1])
        if i[0] in res:
            RESULTS.append('Yes')
        else:
            RESULTS.append('No')

print(*RESULTS, sep='\n')


