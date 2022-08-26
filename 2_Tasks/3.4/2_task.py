import json, pprint


jsn = [
    {'name': 'A', 'parents': []},
    {'name': 'B', 'parents': ['A', 'C']},
    {'name': 'C', 'parents': ['A']},
    {'name': 'D', 'parents': ['B']}
    ]

cls_dict = {}
class_counts = {}
available_classes = []
results = []


def graph(way, point):
    visited_points.append(point)
    if way[point]:
        for top in way[point]:
            graph(way, top)
    else:
        return visited_points


for value in jsn:
    cls_dict[value['name']] = value['parents']
    class_counts[value['name']] = 1
    available_classes.append(value['name'])

for point in available_classes:
    visited_points = []
    results = graph(cls_dict, point)
    print(set(visited_points))
# print(available_classes)
print(class_counts)
# print(cls_dict)






# create_jsondict = json.dumps(jsn)
# print(create_jsondict)
# dict_py = json.loads(create_jsondict)
# print(dict_py)
# pprint.pprint(jsn)