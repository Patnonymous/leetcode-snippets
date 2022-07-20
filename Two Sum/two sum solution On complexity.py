class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Map the processed numbers.
        processedNums = {}

        # Loop through the numbers.
        for index, value in enumerate(nums):
            # Get the remainder.
            remainder = target - nums[index]

            # If the remainder is in our map, then we have the answer.
            if remainder in processedNums:
                return [index, processedNums[remainder]]

            # Add the newest processed number to the list.
            processedNums[value] = index