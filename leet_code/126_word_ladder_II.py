'''
126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s)
from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
import collections

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: List[List[int]]
        """

        ans,q = {},[]
        q.append(beginWord)
        ans[beginWord] = [[beginWord]]
        ans[endWord] = []
        while len(q) != 0:
            tmp = q.pop(0)
            for i in range(len(beginWord)):
                part1,part2 = tmp[:i],tmp[i + 1:]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if tmp[i] != j:
                        newword = part1 + j + part2
                        if newword == endWord:
                            for k in ans[tmp]:
                                ans[endWord].append(k + [endWord])
                            while len(q) != 0:
                                tmp1 = q.pop(0)
                                if len(ans[tmp1][0]) >= len(ans[endWord][0]):
                                    break
                                for ni in range(len(beginWord)):
                                    npart1,npart2 = tmp1[:ni],tmp1[ni+1:]
                                    for nj in "abcdefghijklmnopqrstuvwxyz":
                                        if tmp1[ni] != nj:
                                            nw = npart1 + nj + npart2
                                            if endWord == nw:
                                                for nk in ans[tmp1]:
                                                    ans[endWord].append(nk + [endWord])
                            break
                        if newword in wordList:
                            q.append(newword)
                            ans[newword] = []
                            for k in ans[tmp]:
                                ans[newword].append(k + [newword])
                            wordList.remove(newword)
                        elif newword in ans and len(ans[newword][0]) == len(ans[tmp][0]) + 1:
                            for k in ans[tmp]:
                                ans[newword].append(k + [newword])
        return ans[endWord]


def backtrack(self, result, trace, path, word):
    if len(trace[word]) == 0:
        result.append([word] + path)
    else:
        for prev in trace[word]:
            self.backtrack(result, trace, [word] + path, prev)


def findLadders_2(self, start, end, dict):
    result, trace, current = [], {word: [] for word in dict}, set([start])
    while current and end not in current:
        for word in current:
            dict.remove(word)
        next = set([])
        for word in current:
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    candidate = word[:i] + j + word[i + 1:]
                    if candidate in dict:
                        trace[candidate].append(word)
                        next.add(candidate)
        current = next
    if current:
        self.backtrack(result, trace, [], end)
    return result


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log"]

s = Solution()

print s.findLadders(beginWord, endWord, wordList)
