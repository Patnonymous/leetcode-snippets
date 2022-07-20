class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Alternative solution.

        # Handle "" digits.
        if len(digits) == 0:
            return []


        # Init vars.
        result = []
        # Map the phones letters to the digits.
        phoneDigitsMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}




        def phoneDigitParse(index, currentPath):

            # Current string combo is complete.
            if len(currentPath) == len(digits):
                result.append(currentPath)
                return

            for letter in phoneDigitsMap[digits[index]]:
                phoneDigitParse(index + 1, currentPath + letter)


        phoneDigitParse(0, "")
        return result

