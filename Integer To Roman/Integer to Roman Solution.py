class Solution:
    def intToRoman(self, num: int) -> str:
        print('Running...')

        # Init vars.
        result = ""
        # Order matters for this, list instead of map.
        romanList = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]


        # Loop through the reversed list of roman numerals.
        for romanNumeral, value in reversed(romanList):
            # Integer division will return non-zero for digits we want to use,
            # if not zero then enter the statement and calculate how many roman numerals will be used.
            if num // value:
                romanCount = num // value
                # Python can do int * string for this problem.
                result += (romanNumeral * romanCount)
                # Mod out the value that we already calculated.
                num = num % value
        return result







