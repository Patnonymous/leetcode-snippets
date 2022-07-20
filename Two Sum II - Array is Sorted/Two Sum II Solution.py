class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer method can give O(n) solution.

        # Init vars.
        left = 0
        right = len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right]

            # If the current sum is greater than the target, decrement the right point,
            # if it's less than the target, increment the left pointer
            # Here on leetcode this problem will always have 1 solution.
            if currentSum > target:
                right = right - 1
            elif currentSum < target:
                left = left + 1
            else:
                # Note that the solution indexes for this problem start at 1
                return [left + 1, right + 1]