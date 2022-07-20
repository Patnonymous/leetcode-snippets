class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # Things of note:
        # Diagonal must be dynamic, see numRows = 4 example.
        # Diagonal var starts at numRows - 2, and gets decremented until it's == 1

        resultString = ''
        rowIndex = 0
        colIndex = 0
        # Controls whether to do different processing for diagonal movement.
        doDiagonal = False
        helperGrid = [x[:] for x in [[0] * len(s)] * numRows]


        # Handle numRows = 1
        if numRows == 1:
            return s

        # Handle numRows = 2.
        # Num rows has no diagonal zags.
        if numRows == 2:
            helperGrid = [x[:] for x in [[0] * len(s)] * numRows]
            for letter in s:
                helperGrid[rowIndex][colIndex] = letter
                if rowIndex == numRows - 1:
                    colIndex = colIndex + 1
                    rowIndex = 0
                else:
                    rowIndex = rowIndex + 1
        else:
            # Handle all other numRows.
            # Iterate chars in our string.
            for letter in s:
                # Place a letter on the helper grid.
                helperGrid[rowIndex][colIndex] = letter

                # Do different processing if doDiagonal
                # else, do normal processing.
                if doDiagonal:
                    # If the rowIndex == numRows - 1, then diagonal placement is done.
                    # go back to normal mode, reset rowIndex, and increment colIndex.
                    # Else just decrement rowIndex.
                    if rowIndex == 1:
                        doDiagonal = False
                        rowIndex = 0
                    else:
                        rowIndex = rowIndex - 1
                    colIndex = colIndex + 1
                else:
                    # If rowIndex == numRows - 1, the end of the current col has been reached.
                    # Move to the next col, and enable diagonal mode.
                    # Else, just increment rowIndex.
                    if rowIndex == numRows - 1:
                        colIndex = colIndex + 1
                        doDiagonal = True
                        # Diagonal 'zags' should start at numRows - 2
                        rowIndex = numRows - 2
                    else:
                        rowIndex = rowIndex + 1

        # Iterate through the helperGrid.
        # Ignore 0's, add real letters to the resultString.
        for row in helperGrid:
            for col in row:
                if col != 0:
                    resultString = resultString + col
        return resultString
