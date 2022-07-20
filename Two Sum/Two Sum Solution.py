class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One pass O(n).
        # Use a hash map to save the numbers we have checked, {value: index}
        # If the solution exists, it will be found.

        # Init vars.
        previousMap = {}

        for index, value in enumerate(nums):
            # difference plus the current value is our target.
            difference = target - value
            # Even if we "miss" the first difference because it is not in our map,
            # it will hit it on the second target.
            if difference in previousMap:
                # Note 2sum wants indices, not the values.
                return [previousMap[difference], index]
            # Add to our map.
            previousMap[value] = index
