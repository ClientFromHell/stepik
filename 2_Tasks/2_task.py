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
#

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

# instance_dict = {
#     '1': ['2', '3', '4', '5', '6'],
#     '10': [],
#     '2': ['7', '3', '5', '10', '9'],
#     '3': ['5', '9'],
#     '4': ['10'],
#     '5': ['9'],
#     '6': ['4', '10'],
#     '7': ['8', '3', '5'],
#     '8': ['3', '9'],
#     '9': ['6']
# }

values_for_test = []
# values_for_test = ['winter', 'is', 'coming', 'omg']

# values_for_test = ['ZeroDivisionError', 'OSError', 'ArithmeticError', 'FileNotFoundError']

# values_for_test = ['BaseException', 'KeyError']

# values_for_test = ['base', 'otherBase', 'first', 'second']

# values_for_test = ['5','9','1', '7', '8']


temp_list = []
queue = []
visited = []
temp_results = []
results = []


def dfs(queue, visited, graph):

    """Function makes whole route between required points"""
    while queue:
        for node in queue:
            visited.append(node)
            if node not in graph:
                queue.remove(node)
            else:
                queue += graph[node]
                queue.remove(node)
    return visited


def checker_position(val, res, temp_results):

    """Function checks if a parent covers child, if so, adds child to results"""
    if len(res) == 1:
        temp_results.append(val)
    else:
        for i in res[1:]:
            if i in temp_results:
                if val not in results:
                    results.append(val)
                else:
                    pass
            else:
                temp_results.append(val)



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
    checker_position(i, res, temp_results)

print(*results, sep='\n')
