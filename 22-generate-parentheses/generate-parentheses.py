class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        def solve(op, cl, s):
            if len(s) == 2 * n:
                result.append(s)
                return

            if op < n:
                solve(op + 1, cl, s + "(")
            if cl < op:
                solve(op, cl + 1, s + ")")
        solve(0, 0, "")
        return result