import sys

inherit = []
pointsroute = []
graph = {}
elements = []
queue = []
l_ofresults = []


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
    pointsroute.append(input().split())

for i in inherit:
    elements += i
    if len(i) == 1:
        graph[i[0]] = []
    else:
        graph[i[0]] = i[1:]

elements = set(elements)

for i in pointsroute:

    if i[0] == i[-1]:
        l_ofresults.append('Yes')
    elif i[0] not in elements or i[-1] not in elements:
        l_ofresults.append('No')
    else:
        queue.append(i[-1])
        visited = set()
        res = bfs(queue, visited, graph)
        if i[0] in res:
            l_ofresults.append('Yes')
        else:
            l_ofresults.append('No')

print(*l_ofresults, sep='\n')