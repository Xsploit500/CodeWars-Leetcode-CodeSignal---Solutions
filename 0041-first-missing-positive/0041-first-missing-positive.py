class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
            
        return len(nums) + 1
        
        
        
        
        
        
        nums = set(nums)

        if max(nums) <= 0:
            return 1

        for i in range(1, max(nums) + 2):
            if i not in nums:
                return i

        
        # nums = set(nums)

        # minimum = 1

        # while minimum in nums:
        #     minimum += 1
        
        # if minimum not in nums:
        #     return minimum