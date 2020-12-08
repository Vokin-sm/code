from collections import deque
graph = {}


def create(a):
    if len(a) == 1:
        if a[0] not in graph.keys():
            graph[a[0]] = set()
    else:
        if len(a[1].split()) == 1:
            if a[1] not in graph.keys():
                graph[a[1]] = set()
                graph[a[1]].add(a[0])
                if a[0] not in graph.keys():
                    graph[a[0]] = set()
            else:
                graph[a[1]].add(a[0])
                if a[0] not in graph.keys():
                    graph[a[0]] = set()
        if len(a[1].split()) > 1:
            for el in a[1].split():
                if el not in graph.keys():
                    graph[el] = set()
                    graph[el].add(a[0])
                    if a[0] not in graph.keys():
                        graph[a[0]] = set()
                else:
                    graph[el].add(a[0])
                    if a[0] not in graph.keys():
                        graph[a[0]] = set()


def get(a, b):
    visited = set()
    start_vertex = a
    queue = deque([start_vertex])
    if a not in graph.keys():
        return False
    if b not in graph.keys():
        return False
    if a == b:
        return True
    if b in graph[a]:
        return True
    while queue:
        cur_v = queue.popleft()
        for el in graph[cur_v]:
            if el not in visited:
                visited.add(el)
                queue.append(el)
                if b in graph[el]:
                    return True


def gr():
    n = int(input())
    for i in range(n):
        lst = input().split(":")
        lst = [el.strip() for el in lst]
        create(lst)

    print(graph)

    q = int(input())
    for i in range(q):
        lst = input().split()
        if len(lst) != 2:
            print("No")
        else:
            v_1 = lst[0]
            v_2 = lst[1]
            if get(v_1, v_2):
                print("Yes")
            else:
                print("No")


gr()


