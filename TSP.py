import math
from itertools import combinations


def distance(point1, point2):
        return math.sqrt((points[point1][0] - points[point2][0])**2 + (points[point1][1] - points[point2][1])**2)


def TSP(points, all_vertexes):
    edges = combinations(all_vertexes, 2)
    start, end = min(edges, key=lambda edge: distance(edge[0], edge[1]))


    def add_third(vertex):
        return distance(vertex, start) + distance(vertex, end)
    order = [start, end]
    vertexes = all_vertexes - set(order)
    order.append(min(vertexes, key=add_third))


    def add_vertex(pair):
        first = order[pair[1]]
        second = order[(pair[1] + 1) % len(order)]
        return distance(pair[0], first) + distance(pair[0], second) - distance(first, second)

    length = 3
    while length < n:
        length += 1
        pairs = []
        for index_i in range(len(order)):
            for i in all_vertexes:
                if i not in order:
                    pairs.append((i, index_i))
        i, index_i = min(pairs, key=add_vertex)
        order.insert(index_i + 1, i)
    return order

n = int(input())
points = dict()
all_vertexes = set()
for i in range(n):
    index, x, y = map(float, input().split())
    index = int(index)
    all_vertexes.add(index)
    points[index] = [x,y]

order = TSP(points, all_vertexes)
for i in order:
    print(i, end=' ')
print(order[0])
