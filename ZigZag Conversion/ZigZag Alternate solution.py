class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Sourced from neetcodes tutorial on said problem.
        # Uses a formula to iterate through the rows.
        # Much faster than the helperGrid solution.

        # Other solution
        # Solve using algorithm with no helper grid list.

        # Formula for positions: (numRows - 1) * 2
        # For diagonals: (numRows - 1) * 2 - (2 * current row num)

        # First handle case numRows == 1
        if numRows == 1:
            return s


        # Handle all other cases.
        resultString = ''

        # Process each row.
        for row in range(numRows):
            increment = 2 * (numRows - 1)
            # Process columns.
            for index in range(row, len(s), increment):
                resultString = resultString + s[index]
                # Apply special processing to the diagonals.
                if row > 0 and row < numRows - 1 and index + increment - 2 * row < len(s):
                    resultString = resultString + s[index + increment - 2 * row]
        return resultString