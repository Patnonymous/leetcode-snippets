class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Init initial vars.
        stringLength = len(s)

        # Handle the edge case of 1 character long strings.
        if stringLength < 2:
            return s


        # Init palindrome helper vars.
        # Start is the starting index of the longest palindrome.
        start = 0
        # Result length is the length of the longest palindrome. Starts at 1.
        resultLength = 1


        # Loop through the length of the string.
        for index in range(stringLength):
            # We an use a low boundary and a high boundary to a create a "window" to
            # help search for the palindrome.
            # Lower bound is one less than current index.
            boundLow = index - 1
            # High bound is one more than the current index.
            boundHigh = index + 1
            # For example, if "babad" search was on the index of 1 (so the first a)
            # boundLow would start at the first b, boundHigh would start at the second b.


            # The first two checks check the chars at the bound index against
            # the char at index.
            # Helps with strings where there are multiple of the same chars in a row.
            # The final check is pretty straightforward, it checks if the char at the bound
            # equals the char at the other bound, and adjusts vars if true.


            # While high bound is less than the length of s,
            # and the character at boundHigh index is equal to char at index,
            # increase boundHigh by 1.
            while boundHigh < stringLength and s[boundHigh] == s[index]:
                boundHigh = boundHigh + 1

            # While boundLow is greater than or equal to 0,
            # and the char at boundLow index is equal to the char at index,
            # Decrease the boundLow by 1
            while boundLow >= 0 and s[boundLow] == s[index]:
                boundLow = boundLow - 1

            # While boundLow is greater than or equal to 0,
            # and boundHigh is greater than the length of s,
            # and the char at boundLow index is equal to the char at boundHigh index,
            # Increase and decrease the vars.
            while boundLow >= 0 and boundHigh < stringLength and s[boundLow] == s[boundHigh]:
                boundHigh = boundHigh + 1
                boundLow = boundLow - 1


            # Now do length checks, and adjust vars.
            substringLength = boundHigh - boundLow - 1
            if resultLength < substringLength:
                resultLength = substringLength
                start = boundLow + 1

        # Finally, return the palindrome.
        # Add start to the resultLength to offset the start,
        # otherwise length will be wrong.
        resultPalindrome = s[start:start + resultLength]
        return resultPalindrome