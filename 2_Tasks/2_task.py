import pprint

instance_dict = {}

# instance_dict = {
#     'coming': [],
#     'is': [],
#     'omg': ['winter', 'is', 'coming'],
#     'winter': []
# }

# instance_dict = {
#     'ArithmeticError': [],
#     'FileNotFoundError': ['OSError'],
#     'OSError': [],
#     'ZeroDivisionError': ['ArithmeticError']}


# instance_dict = {
#     'BaseException': [],
#     'Exception': ['BaseException'],
#     'LookupError': ['Exception'],
#     'KeyError': ['LookupError']}


# instance_dict = {
#     'base': [],
#     'first': ['otherBase'],
#     'otherBase': [],
#     'second': ['base']
# }

values_for_test = []
# values_for_test = ['winter', 'is', 'coming', 'omg']

# values_for_test = ['ZeroDivisionError', 'OSError', 'ArithmeticError', 'FileNotFoundError']

# values_for_test = ['BaseException', 'KeyError']

# values_for_test = ['base', 'otherBase', 'first', 'second']

temp_list = []
queue = []
visited = []
temp_results = []
results = []


def dfs(queue, visited, graph):
    while queue:
        for node in queue:
            visited.append(node)
            if node not in graph:
                queue.remove(node)
            else:
                queue += graph[node]
                queue.remove(node)
    return visited


def checker_position(val, res):
    if len(res) == 1:
        temp_results.append(val)
    else:
        for i in res:
            if i in temp_results and val not in results:
                if val not in results:
                    results.append(val)
            else:
                pass

for _ in range(int(input())):
    temp_list += [input().replace(':', '').strip().split()]

for _ in range(int(input())):
    values_for_test += [input().strip()]

for i in temp_list:
    if len(i) == 1:
        instance_dict[i[0]] = []
    else:
        instance_dict[i[0]] = i[1:]

for i in values_for_test:
    visited = []
    queue.append(i)
    res = dfs(queue, visited, instance_dict)
    checker_position(i, res)

# pprint.pprint(instance_dict)
# pprint.pprint(values_for_test)
print(*results, sep='\n')
