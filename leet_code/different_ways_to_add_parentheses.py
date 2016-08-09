'''
241. Different Ways to Add Parentheses
Given a string of numbers and operators, return all possible results from computing all the different possible
ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

'''


class Solution(object):
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i in xrange(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i + 1:])
                for j in res1:
                    for k in res2:
                        res.append(self.calculate(j, k, input[i]))
        return res

    def calculate(self, m, n, op):
        if op == "+":
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n

    def diffWaysToCompute_p(self, input):
        """
        :type input: str
        :rtype: List[int]
        """

        return [a + b if c == '+' else a - b if c == '-' else a * b
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i + 1:])
                ] or [int(input)]


s = Solution()

print s.diffWaysToCompute("2-1-1")
