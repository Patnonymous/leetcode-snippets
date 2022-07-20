class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # Regression without cache
        # Sourced from neetcode
        # Slow and inefficient without caching!

        def backtrackSearch(i, j):
            # i and j out of bounds is a match
            if i >= len(s) and j >= len(p):
                return True
            # j out of bounds, there's unmatchable string
            # not a match.
            if j >= len(p):
                return False

            # Include i and j boundary checks to prevent
            # index out of range exceptions.
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if (j + 1) < len(p) and p[j + 1] == '*':
                return backtrackSearch(i, j + 2) or (match and backtrackSearch(i + 1, j))

            if match:
                return backtrackSearch(i + 1, j + 1)

            return False
        return backtrackSearch(0, 0)