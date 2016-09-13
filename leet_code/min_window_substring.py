'''
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

'''

import collections


class Solution(object):
    # http://www.tangjikai.com/algorithms/leetcode-76-minimum-window-substring
    def minWindow(self, s, t):
        res = ''
        window = []
        dic = collections.defaultdict(list)
        tCount = collections.Counter(t)

        for i, c in filter(lambda x: x[1] in t, enumerate(s)):
            if len(dic[c]) == tCount[c]:
                window.remove(dic[c].pop(0))

            dic[c].append(i)
            window.append(i)

            if len(window) == len(t) and (res == '' or window[-1] - window[0] < len(res)):
                res = s[window[0]: window[-1] + 1]

        return res

    def minWindow_9(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if (t == ""):
            return ""
        d, dt = {}, dict.fromkeys(t, 0)
        for c in t:
            d[c] = d.get(c, 0) + 1
        pi, pj, cont = 0, 0, 0
        if (s == "" or t == ""):
            return ""
        ans = ""
        while pj < len(s):
            if s[pj] in dt:
                if dt[s[pj]] < d[s[pj]]:
                    cont += 1
                dt[s[pj]] += 1
            if cont == len(t):
                while pi < pj:
                    if s[pi] in dt:
                        if dt[s[pi]] == d[s[pi]]:
                            break
                        dt[s[pi]] -= 1
                    pi += 1
                if ans == '' or pj - pi < len(ans):
                    ans = s[pi:pj + 1]
                dt[s[pi]] -= 1
                pi += 1
                cont -= 1
            pj += 1
        return ans


source = "ADOBECODEBANC"
target = "ABC"

s = Solution()
print s.minWindow(source, target)
