class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Reverse and checking without string.
        # Use modulo and division to "cut" the number in half.
        reversedNum = 0
        temp = x

        while temp > 0:
            # temp % 10: get last digit
            # reversedNum * 10: get proper place for the new digit
            reversedNum = reversedNum * 10 + temp % 10
            # Remove the last digit from temp
            temp = floor(temp / 10)

        # Return equality.
        return x == reversedNum

