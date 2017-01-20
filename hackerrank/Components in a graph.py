# n = int(raw_input())
gb = [
    [1, 6],
    [2, 7],
    [3, 8],
    [4, 9],
    [2, 6]
]

n = 5
edges_set = []
min_com = 15000
max_com = 0
for i in range(n):
    # g, b = raw_input().strip().split(" ")
    g, b = gb[i]
    new_edges = set()
    new_edges.add(g)
    new_edges.add(b)
    i = 0
    while i < len(edges_set):  # do not use "for edges in edges_set" here!
        if g in edges_set[i] or b in edges_set[i]:
            new_edges = new_edges | edges_set[i]
            edges_set.pop(i)
        else:
            i += 1
    edges_set.append(new_edges)

    if min_com > len(new_edges):
        min_com = len(new_edges)
    if max_com < len(new_edges):
        max_com = len(new_edges)

# sorted_edges = sorted(edges_set, key=lambda k: len(k))
#
# print len(sorted_edges[0]), len(sorted_edges[-1])

print min_com, max_com

# ----- Version 1 ,  Timeout!
n = int(raw_input())
edges_set = []
for i in range(n):
    g, b = raw_input().strip().split(" ")
    new_edges = set()
    new_edges.add(g)
    new_edges.add(b)
    i = 0
    while i < len(edges_set):  # do not use "for edges in edges_set" here!
        if g in edges_set[i] or b in edges_set[i]:
            new_edges = new_edges | edges_set[i]
            edges_set.pop(i)
        else:
            i += 1

    edges_set.append(new_edges)
sorted_edges = sorted(edges_set, key=lambda k: len(k))

print len(sorted_edges[0]), len(sorted_edges[-1])

# ----- Version 2 ,  Timeout!
n = int(raw_input())
edges_set = []
for i in range(n):
    g, b = raw_input().strip().split(" ")
    g, b = int(g), int(b)
    new_edges = set()
    new_edges.add(g)
    new_edges.add(b)
    i = 0
    while i < len(edges_set):  # do not use "for edges in edges_set" here!
        if g in edges_set[i] or b in edges_set[i]:
            new_edges = new_edges | edges_set[i]
            edges_set.pop(i)
        else:
            i += 1

    edges_set.append(new_edges)

min_com = 15001
max_com = 0
for e in edges_set:
    com = len(e)
    if min_com > com:
        min_com = com
    if max_com < com:
        max_com = com

print min_com, max_com

