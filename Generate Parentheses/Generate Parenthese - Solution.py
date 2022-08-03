class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # There are crazy Python tricks to shorten this to a few lines.
        
        
        # Init vars.
        current = []
        result = []
        
        def backtrack(opened, closed):
            # If opened, closed and n are equal, append to result and return out of the instance.
            if opened == closed == n:
                result.append(''.join(current))
                return
            
            # If opened is less than n, add an open parentheses.
            if opened < n:
                current.append('(')
                backtrack(opened + 1, closed)
                current.pop()
            
            # If opened is greater than closed, add a closing parentheses.
            if closed < opened:
                current.append(')')
                backtrack(opened, closed + 1)
                current.pop()
        
        # Start backtrack and return final.
        backtrack(0, 0)
        return result