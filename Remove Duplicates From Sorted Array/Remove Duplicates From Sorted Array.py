class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Init vars.
        # We start at index 1, the list is non-descending so index 0 will never be changed.
        left = 1
        
        # Edge case: len(nums) == 1
        if len(nums) == 1:
            return 1
        
        # Main loop
        for right in range (1, len(nums)):
            # If the current number is different than the previous
            # Set the left index as this number, then increment the left index.
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
           
        
        # With the way this is coded, left can be our K value.
        return left
            