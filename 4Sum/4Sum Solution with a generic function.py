class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # See Two Sum II and 3sum strategies.
        # Rather than hardcode into 4Sum, can this be solved with a generic algorithm?
        # Eg. KSum where K is a number > 2


        # Init vars.
        result = []
        quad = []
        nums.sort()

        def kSum(k, start, target):
            if k != 2:
                for index in range(start, len(nums) - k + 1):
                    # Avoid duplicates.
                    if index > start and nums[index] == nums[index - 1]:
                        continue


                    quad.append(nums[index])
                    kSum(k - 1, index + 1, target - nums[index])
                    quad.pop()
                return

            # Two Sum base case.
            left = start
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append(quad + [nums[left], nums[right]])
                    left += 1
                    # Avoid duplicates.
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        # Run and return.
        kSum(4, 0, target)
        return result
