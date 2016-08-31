'''
274. H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute
the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least
h citations each, and the other N - h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had
received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and
the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.


reference :
    https://www.hrwhisper.me/leetcode-h-index-h-index-ii/
'''


class Solution(object):
    # h-index = min (i, citation[i])
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        return max([min(i + 1, c) for i, c in enumerate(sorted(citations, reverse=True))])
        # return max([min(len(citations) - i, c) for i, c in enumerate(sorted(citations))])
