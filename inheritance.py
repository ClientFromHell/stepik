import sys

inherit = []
CLS_CHECKER = []
DICT_CLASS = {}
elements = []
queue = []
RESULTS = []


def bfs(queue, visited, graph):
    while queue:
        for node in queue:
            visited.add(node)
            if node not in graph:
                queue.remove(node)
            else:
                queue += graph[node]
                queue.remove(node)
    return visited


for i in range(int(sys.stdin.readline())):
    inherit.append(input().replace(':', '').split())

for i in range(int(sys.stdin.readline())):
    CLS_CHECKER.append(input().split())

for i in inherit:
    elements += i
    if len(i) == 1:
        DICT_CLASS[i[0]] = []
    else:
        DICT_CLASS[i[0]] = i[1:]

elements = set(elements)

for i in CLS_CHECKER:

    if i[0] == i[-1]:
        RESULTS.append('Yes')
    elif i[0] not in elements or i[-1] not in elements:
        RESULTS.append('No')
    else:
        queue.append(i[-1])
        visited = set()
        res = bfs(queue, visited, DICT_CLASS)
        if i[0] in res:
            RESULTS.append('Yes')
        else:
            RESULTS.append('No')

print(*RESULTS, sep='\n')