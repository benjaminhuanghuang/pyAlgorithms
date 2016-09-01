'''
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented
as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

'''

import collections


class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        left = min(x[0] for x in rectangles)
        bottom = min(x[1] for x in rectangles)
        right = max(x[2] for x in rectangles)
        top = max(x[3] for x in rectangles)

        points = collections.defaultdict(int)
        for l, b, r, t in rectangles:
            A, B, C, D = (l, b), (r, b), (r, t), (l, t)
            for p, q in zip((A, B, C, D), (1, 2, 4, 8)):
                if points[p] & q:
                    return False
                points[p] |= q

        for px, py in points:
            if left < px < right or bottom < py < top:
                if points[(px, py)] not in (3, 6, 9, 12, 15):
                    return False
        return True

    def isRectangleCover_2(self, rectangles):
        """ :type rectangles: List[List[int]] :rtype: bool """

        def recordCorner(point):
            if point in corners:
                corners[point] += 1
            else:
                corners[point] = 1

        corners = {}
        area = 0
        left = min(x[0] for x in rectangles)
        bottom = min(x[1] for x in rectangles)
        right = max(x[2] for x in rectangles)
        top = max(x[3] for x in rectangles)

        for sub in rectangles:
            ax, ay, bx, by = sub[:]
            area += (bx - ax) * (by - ay)
            map(recordCorner, [(ax, ay), (bx, by), (ax, by), (bx, ay)])

        if area != (top - bottom) * (right - left):
            return False

        big_four = [(left, bottom), (right, top), (left, top), (right, bottom)]

        for bf in big_four:  # check corners of big rectangle
            if bf not in corners or corners[bf] != 1:
                return False

        for key in corners:  # check existing "inner" points
            # all corner point display 2 or 4 times, except 4 big corner
            if corners[key] % 2 and key not in big_four:
                return False

        return True


rectangles = [
    [1, 1, 3, 3],
    [3, 1, 4, 2],
    [1, 3, 2, 4],
    [2, 2, 4, 4]
]

rectangles = [[0, 0, 2, 2], [1, 1, 3, 3], [2, 0, 3, 1], [0, 3, 3, 4]]
rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
s = Solution()
s.isRectangleCover_2(rectangles)
