class Solution:
    def longestPalindrome(self, s: str) -> str:
        stLen = len(s)

        # Handle small strings.
        if (stLen < 2):
            return s[:stLen]

        # Handle palindrome checks.
        start = 0
        resultLen = 1

        # For range of length of string.
        for index in range(stLen):
            # Lower boundary, and higher boundary.
            # Set according to index each iteration.
            radLow = index - 1
            radHigh = index + 1

            # While high boundary is under the length of string
            # and the char at the high boundary is equal to the char at index
            # increment the higher boundary.
            while radHigh < stLen and s[radHigh] == s[index]:
                radHigh = radHigh + 1

            # While low boundary is under or equal zero
            # and the char at low boundary is equal to char at index
            # decrement the lower boundary.
            while radLow >= 0 and s[radLow] == s[index]:
                radLow = radLow - 1

            # While low boundary is under or equal to zero
            # and high boundary is under length of string
            # and the char at low boundary is equal to char at higher boundary
            # Increment high boundary, decrement lower boundary.
            while radLow >= 0 and radHigh < stLen and s[radLow] == s[radHigh]:
                radHigh = radHigh + 1
                radLow = radLow - 1

            # Set the substring length.
            subLen = radHigh - radLow - 1
            # Do the check for the palindrome length.
            # If it's bigger, set result length to current substring length.
            # and set the start to the low bound plus one.
            if resultLen < subLen:
                resultLen = subLen
                start = radLow + 1

        # Return the palindrome substring.
        resultPal = s[start:start + resultLen]
        return resultPal