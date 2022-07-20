class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Converting to string solution.
        # Ye olde slow solution.
        # Lets see if it times out.
        asString = str(x)
        return asString == asString[::-1]
