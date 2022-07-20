class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Recursive Solution by OvsovNikita on leetcode.

        nums.sort()
        return self.KSumClosest(nums, 3, target)


    # Find the closest sum of K numbers to the target.
    def KSumClosest(self, nums: List[int], k: int, target: int) -> int:

        numsListLength = len(nums)

        # Handles nums list where the length is the same size as
        # K.
        if numsListLength == k:
            return sum(nums[:k])


        # Return current if the first K values are greater or equal than target.
        # nums[:k] is a slice getting the first K indicies.
        current  = sum(nums[:k])
        if current >= target:
            return current

        # Return current if the last K values are greater or equal than target.
        current = sum(nums[-k:])
        if current <= target:
            return current

        # Special case if K is 1.
        if k == 1:
            return min([(x, abs(target - x)) for x in nums], key = lambda x: x[1])[0]

        # Set closest as sum of first k values.
        closest = sum(nums[:k])

        # Enumerate nums.
        for index, value in enumerate(nums[:-k+1]):
            # Avoid duplicates.
            if index > 0 and value == nums[index - 1]:
                continue

            # Recursively call KSumClosest.
            # Passes in nums with current index + 1 cut off from the start.
            # Passes in K with 1 decremented.
            # Target is current target minus the current value.
            current = self.KSumClosest(nums[index+1:], k-1, target - value) + value

            if abs(target - current) < abs(target - closest):
                if current == target:
                    return target
                else:
                    closest = current
        return closest


