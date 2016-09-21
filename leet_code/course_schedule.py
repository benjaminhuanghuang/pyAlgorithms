'''
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0
you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how
a graph is represented.


Reference
    https://www.hrwhisper.me/leetcode-graph/
    http://www.kangry.net/blog/?type=article&article_id=203
'''


class Solution(object):
    # http://bookshadow.com/weblog/2015/05/07/leetcode-course-schedule/
    # http://bookshadow.com/weblog/2015/05/14/leetcode-course-schedule-ii/
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0] * numCourses
        childs = [[] for x in range(numCourses)]
        for pair in prerequisites:
            degrees[pair[0]] += 1
            childs[pair[1]].append(pair[0])

        courses = set(range(numCourses))
        flag = True

        while flag and len(courses):
            flag = False
            removeList = []
            for x in courses:
                if degrees[x] == 0:
                    for child in childs[x]:
                        degrees[child] -= 1
                    removeList.append(x)
                    flag = True
            for x in removeList:
                courses.remove(x)
        return len(courses) == 0

    # http://www.tangjikai.com/algorithms/leetcode-207-208-course-schedule-i-ii
    # If all nodes have in-degree, the graph has a cycle, no solution.
    # According the method of topological sort, remove the nodes without in-degree one by one.
    def canFinish(self, numCourses, prerequisites):
        # zeroInDegree stores nodes without in-degree and degree puts number of in-degree for each node.
        zeroInDegree = set()
        degree = [0] * numCourses

        for pre in prerequisites:
            degree[pre[0]] += 1

        for i in range(len(degree)):
            if degree[i] == 0:
                zeroInDegree.add(i)

        if not zeroInDegree:
            return False

        while zeroInDegree:
            it = iter(zeroInDegree)
            course = it.next()
            zeroInDegree.remove(course)

            for i in range(len(prerequisites)):
                edge = prerequisites[i]
                if edge[1] == course:
                    degree[edge[0]] -= 1
                    if degree[edge[0]] == 0:
                        zeroInDegree.add(edge[0])

        return sum(degree) == 0


    # http://www.tangjikai.com/algorithms/leetcode-207-208-course-schedule-i-ii
    # If node v has not been visited, then mark it as 0.
    # If node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then there is a cycle.
    # If node v has been visited, then mark it as 1. If a vertex was marked as 1, then no cycle contains v or its successors.
    def canFinish_DFS(self, numCourses, prerequisites):
        graph = [[] for x in range(numCourses)]
        visited = [0] * numCourses

        for course, pre in prerequisites:
            graph[course].append(pre)

        for i in range(numCourses):
            if not self.dfs(i, visited, graph):
                return False
        return True

    def dfs(self, course, visited, graph):
        if visited[course] == -1:
            return False
        elif visited[course] == 1:
            return True

        visited[course] = -1
        for j in graph[course]:
            if not self.dfs(j, visited, graph):
                return False
        visited[course] = 1
        return True
n = 2
ps = [[1, 0]]
s = Solution()
print s.canFinish(n, ps)
