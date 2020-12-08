import json

graph = dict()

with open("graph_json.json", "r") as f:
    graphs = json.load(f)

for gr in graphs:
    for g in gr["parents"]:
        if g not in graph.keys():
            graph[g] = set()
            graph[g].add(gr["name"])
        graph[g].add(gr["name"])
    for gra in graphs:
        if gra["name"] not in graph.keys():
            graph[gra["name"]] = set()


def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex])
    return len(visited)


print(graph)
print(graphs)

for gr in sorted(list(graph.keys())):
    print(gr + " : " + str(dfs(graph, gr)))








