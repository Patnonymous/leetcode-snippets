class Solution:
    def isValid(self, s: str) -> bool:

        # O(n) solution.

        # Keep track of opened parenthese.
        # Opened stack isnt empty then return False.
        openedStack = []
        # Map the closing to the opening.
        closeOpenMap = {')':'(', '}':'{', ']':'['}


        for letter in s:
            if letter in closeOpenMap:
                # Pops if appropriate.
                # Remember the brackets must close in the correct order,
                # so if the sequence is "broke", return False right here.
                if openedStack and openedStack[-1] == closeOpenMap[letter]:
                    openedStack.pop()
                else:
                    return False
            else:
                # Thanks to the constraint that s will only contain ()[]{},
                # we can just append here.
                openedStack.append(letter)

        # Return answer.
        return True if not openedStack else False