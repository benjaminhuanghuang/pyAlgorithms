'''

'''

from collections import defaultdict


class Graph(object):
    def __init__(self, count):
        self.node_count = count
        self.edges = defaultdict(list)

    def connect(self, n1, n2):
        self.edges[n1].append(n2)
        self.edges[n2].append(n1)

    def find_all_distances(self, start_node):
        distances = [-1 for i in range(self.node_count)]
        unvisited = set([i for i in range(self.node_count)])
        q = []

        distances[start_node] = 0
        unvisited.remove(start_node)
        q.append(start_node)

        while not len(q) > 0:
            node = q[0]
            children = self.edges[node]
            height = distances[node]
            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    q.append(child)

        distances.pop(start_node)

        print(" ".join(map(str, distances)))


'''
t = input()
for i in range(t):
    n, m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x, y = [int(x) for x in raw_input().split()]
        graph.connect(x - 1, y - 1)
    s = input()
    graph.find_all_distances(s - 1)
'''
# number of nodes
n = 4
# number of edges
m = 2

# connects:
con = [[1, 2], [1, 3]]

graph = Graph(n)
for i in con:
    graph.connect(i[0] - 1, i[1] - 1)

start = 1
graph.find_all_distances(start - 1)
