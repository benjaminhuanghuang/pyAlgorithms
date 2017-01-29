'''
http://www.lintcode.com/en/problem/topological-sorting/?source=lxhwechat


Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

 Notice

You can assume that there is at least one topological order in the graph.
'''


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """

    def topSort(self, graph):
        # write your code here
        # r
        if not graph:
            return []
        count_in_degree = {}
        for node in graph:
            count_in_degree[node] = 0

        for node in graph:
            for neighober in node.neighbors:
                count_in_degree[neighober] = count_in_degree[neighober] + 1

        ans = []
        for node in graph:
            if count_in_degree[node] == 0:
                self.dfs(node, count_in_degree, ans)
        return ans

    def dfs(self, node, count_in_degree, ans):
        ans.append(node)
        count_in_degree[node] -= 1
        for neighbor in node.neighbors:
            count_in_degree[neighbor] = count_in_degree[neighbor] - 1
            if count_in_degree[neighbor] == 0:
                self.dfs(neighbor, count_in_degree, ans)


s = Solution()
start = DirectedGraphNode(1)
start.neighbors.append(DirectedGraphNode(2))
start.neighbors.append(DirectedGraphNode(3))
s.topSort(DirectedGraphNode(1))
