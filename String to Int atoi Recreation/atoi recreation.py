class Solution:
    def myAtoi(self, s: str) -> int:

        # L strip whitespace.
        s = s.lstrip()

        # Handle empty.
        if len(s) == 0:
            return 0
        result = 0
        min32 = 2 ** 31

        # Start index.
        startIndex = 0

        # Multiplier for negatives, and to skip + and - characters.
        multi = 1
        if s[0] == '-':
            multi = -1
            startIndex = 1
        elif s[0] == '+':
            startIndex = 1

        index = startIndex
        while index < len(s):
            # Use asci values to handle non numeric.
            if not ('0' <= s[index] <= '9'):
                return result * multi

            # Result * 10 for correct base position.
            # Asci value of current char minus asci value of 0
            #result = result * 10 + ord(s[index]) - ord('0')
            result = result * 10 + int(s[index])

            # Range clamping.
            if result * multi <= -min32:
                return -min32
            elif result * multi  >= min32 - 1:
                return min32 - 1
            index = index + 1

        # Return result according to the multiplier (handles positive or negative)
        return result * multi
