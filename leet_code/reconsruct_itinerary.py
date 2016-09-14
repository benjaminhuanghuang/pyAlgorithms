'''
332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the
itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when
    read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

    All airports are represented by three capital letters (IATA code).

    You may assume all tickets form at least one valid itinerary.

Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.


'''
import collections


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        result = ["JFK"]

        # if key does not exist, call list() to create a default value for the key
        dic = collections.defaultdict(list)
        for t in tickets:
            dic[t[0]] += t[1],

        self.dfs_helper(dic, "JFK", result, len(tickets))

        return result

    def dfs_helper(self, dic, departure, result, flights):
        if len(result) == flights + 1:
            return result

        currentDst = sorted(dic[departure])
        for dst in currentDst:
            dic[departure].remove(dst)
            result.append(dst)

            valid = self.dfs_helper(dic, dst, result, flights)
            if valid:
                return valid

            result.pop()
            dic[departure].append(dst)


tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
s = Solution()

print s.findItinerary(tickets)

a = []
# a = a + "dddd"

a += "dddd"
a += "dddd"
print a
