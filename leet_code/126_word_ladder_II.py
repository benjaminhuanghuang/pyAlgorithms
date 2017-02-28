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


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: List[List[int]]
        """

        def buildPath(path, word):
            if len(preMap[word]) == 0:
                result.append([word] + path)
                return
            path.insert(0, word)
            for w in preMap[word]:
                buildPath(path, w)
            path.pop(0)

        length = len(beginWord)
        preMap = {}
        for word in wordList:
            preMap[word] = []
        result = []
        cur_level = set()
        cur_level.add(beginWord)

        while True:
            pre_level = cur_level
            cur_level = set()
            for word in pre_level:
                wordList.remove(word)

            for word in pre_level:
                for i in range(length):
                    left = word[:i]
                    right = word[i + 1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            nextWord = left + c + right
                            if nextWord in wordList:
                                preMap[nextWord].append(word)
                                cur_level.add(nextWord)
            if len(cur_level) == 0:
                return []
            if endWord in cur_level:
                break
        buildPath([], endWord)
        return result

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

s.findLadders(beginWord, endWord, wordList)
