from struct import pack, error

class Solution:
    def reverse(self, x: int) -> int:

        # int to str
        asString = str(x)


        # Handles negatives and positive.
        if asString[0] == '-':
            asString = '-' + asString[:0:-1]
        else:
            asString = asString[::-1]

        # To result, then return.
        resultInt = int(asString)

        #32 bit check.
        try:
            pack("i", resultInt)
        except error:
            return 0

        return resultInt