class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Two var method.

        # Init vars.
        resultArea = 0
        boundStart = 0
        boundEnd = len(height) - 1


        while boundStart < boundEnd:
            # Get the new area.
            # Note boundEnd - boundStart to account for the different start positions.
            # Use min to get the smaller height.
            waterArea = (boundEnd - boundStart) * min(height[boundStart], height[boundEnd])

            # Get the greater area.
            resultArea = max(resultArea, waterArea)

            # If the height at boundStart is less than the height at boundEnd,
            # increment boundStart.
            # Else decrement boundEnd.
            # Eventually they will hit eachother and trigger the while loops exit condition.
            if height[boundStart] < height[boundEnd]:
                boundStart = boundStart + 1
            else:
                boundEnd = boundEnd - 1

        # Return the result.
        return resultArea
