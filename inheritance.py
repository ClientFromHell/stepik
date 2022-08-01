import collections, sys, pprint


# TESTS:

DICT_CLASS = {
    'A': ['B', 'C', 'D', 'G', 'H'],
    'B': ['C', 'E', 'G', 'H', 'K', 'L'],
    'C': ['E', 'D', 'H', 'K', 'L'],
    'D': ['G', 'H'],
    'E': ['D', 'F', 'K', 'L'],
    'F': ['K'],
    'G': ['F'],
    'H': ['L'],
    'K': ['H', 'L'],
    'L': []
                  }

CLS_CHECKER = [
                 ['K', 'D'],
                 ['D', 'A'],
                 ['G', 'D'],
                 ['H', 'A'],
                 ['E', 'E'],
                 ['H', 'G'],
                 ['E', 'L'],
                 ['D', 'L'],
                 ['B', 'D'],
                 ['D', 'G'],
                 ['D', 'E'],
                 ['A', 'F'],
                 ['A', 'C'],
                 ['K', 'A'],
                 ['A', 'H'],
                 ['K', 'D'],
                 ['H', 'B'],
                 ['K', 'B'],
                 ['D', 'L'],
                 ['G', 'G'],
                 ['A', 'H'],
                 ['K', 'L'],
                 ['G', 'E'],
                 ['B', 'A'],
                 ['C', 'K'],
                 ['K', 'L'],
                 ['C', 'L'],
                 ['G', 'C'],
                 ['D', 'D'],
                 ['C', 'G'],
                 ['E', 'A'],
                 ['F', 'K'],
                 ['B', 'G'],
                 ['H', 'L'],
                 ['L', 'F'],
                 ['H', 'G'],
                 ['D', 'A'],
                 ['H', 'L']
               ]


# DICT_CLASS = {}
# CLS_CHECKER = []
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


# for i in range(int(sys.stdin.readline().strip())):
#     inherit.append([num for num in filter(lambda num: num.isalpha(), sys.stdin.readline().strip())])
#
# for i in range(int(sys.stdin.readline())):
#     CLS_CHECKER.append(sys.stdin.readline().strip().split())

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

# print(RESULTS)
# print(*RESULTS, sep='\n')
