class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Using sorting and two pointer strategies from Two Sum II, this
        # problem can be solved with O(n^2)


        result = []
        nums.sort()

        for index, firstNum in enumerate(nums):
            # Avoid duplicates by using continue.
            if index > 0 and firstNum == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                threeSum = firstNum + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([firstNum, nums[left], nums[right]])
                    left += 1
                    # Increment left to avoid duplicates.
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result