class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # This can use digits 2-9 inclusive.
        # Total number of digits input can be 0-4 inclusive.


        # Handle case where digits length is 0.
        if len(digits) == 0:
            return []


        # Init vars.
        result = []
        # Map the phones letters to the digits.
        phoneDigitsMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


        # Each "path" is a combination of letters which will be appended to the result.
        def phoneParse(index, path):

            # Note that the combination of letters will always be the same length as the provided
            # digits. Therefore once this is True, we have finished a combo
            # and should add it to the result.
            if len(path) == len(digits):
                result.append(''.join(path))
                return

            # Initially our available letters will be all the letters associated with the respective
            # phone number digit.
            # For example: If our input digits are "35", and we start at index of 0,
            # the availableLetters will be phoneDigitsMap[digits[0]] which is digit 3, "def".
            # (see the phone digit map near the start)
            availableLetters = phoneDigitsMap[digits[index]]


            # Iterate through the available letters.
            for letter in availableLetters:
                # Append the current letter to our path.
                path.append(letter)
                # Call phoneParse again to work on the next digit.
                phoneParse(index + 1, path)
                # Pop off the top digit.
                # Consider the following: Test case is "359", so the result will end up with combos with length of 3.
                # While backtracking, call phoneParse for first letter of 3: "d", the first letter of 5: "j",
                # then we go to work on the "end": the letters for 9.
                # The first end letter we hit is "w". So that path is "djw". w is no longer needed, this path.pop() will pop
                # off the "w" so then the next letter "x" can be properly added to the end of the path.
                # Once all the "dj*" is finished, it backtracks and pop off the "j" so the algorithm can then work on
                # "dk*" and so on and so forth.
                path.pop()

        # Start recursive function.
        phoneParse(0, [])
        return result